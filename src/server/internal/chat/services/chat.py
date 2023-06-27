import grpc
import tortoise.exceptions

import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
import src.server.internal.auth.entities.user as user
import src.server.internal.chat.entities.event as event
import src.server.internal.chat.entities.event_queue as event_queue
import src.server.internal.chat.entities.message as message


class ChatService(chat_service_pb2_grpc.ChatServiceServicer):
    async def Send(self, request, context):
        userId = context.user_id

        if not request.content:
            context.set_details("Content is empty")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        newMessage = await message.Message.create(
            user_id=userId, content=request.content
        )

        # NOTE: Create new event
        await event.Event.create(
            user_id=userId,
            object_id=newMessage.id,
            type=event.EventType.MESSAGE,
        )

        return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    async def GetMessage(self, request, context):
        userId = context.user_id

        if not request.message_id:
            context.set_details("Message ID is empty")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        msg = await message.Message.filter(
            id=request.message_id, user_id=userId
        ).first()

        if not msg:
            context.set_details("Message not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        sendUser = await user.User.get(id=msg.user_id)

        reactions = await msg.reactions.all()

        newReactions = []
        for reaction in reactions:
            reactionUser = await user.User.get(id=reaction.user_id)

            newReactions.append(
                chat_service_pb2.Reaction(
                    user_id=f"{reactionUser.id}",
                    user_name=f"{reactionUser.user_name}",
                )
            )

        return chat_service_pb2.Message(
            message_id=f"{msg.id}",
            user_id=f"{msg.user_id}",
            user_name=sendUser.user_name,
            content=msg.content,
            reactions=newReactions,
            created_time=f"{msg.created_time}",
        )

    async def React(self, request, context):
        userId = context.user_id

        isUserReacted = await message.Reaction.filter(
            user_id=userId, message_id=request.message_id
        ).exists()

        if isUserReacted:
            context.set_details("User already reacted")
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        newReaction = await message.Reaction.create(
            user_id=userId, message_id=request.message_id
        )

        # NOTE: Create new event
        await event.Event.create(
            user_id=userId,
            object_id=newReaction.id,
            type=event.EventType.REACTION,
        )

        return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    async def GetReaction(self, request, context):
        if not request.reaction_id:
            context.set_details("Reaction ID is empty")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

        try:
            reaction = await message.Reaction.get(id=request.reaction_id)
            reactionUser = await user.User.get(id=reaction.user_id)

            return chat_service_pb2.Reaction(
                user_id=f"{reactionUser.id}",
                user_name=f"{reactionUser.user_name}",
            )
        except tortoise.exceptions.DoesNotExist:
            context.set_details("Reaction not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return chat_service_pb2.google_dot_protobuf_dot_empty__pb2.Empty()

    async def Fetch(self, request, context):
        messages = await message.Message.all()

        for msg in messages:
            sendUser = await user.User.get(id=msg.user_id)

            reactions = await msg.reactions.all()

            newReactions = []
            for reaction in reactions:
                reactionUser = await user.User.get(id=reaction.user_id)

                newReactions.append(
                    chat_service_pb2.Reaction(
                        user_id=f"{reactionUser.id}",
                        user_name=f"{reactionUser.user_name}",
                    )
                )

            yield chat_service_pb2.Message(
                message_id=f"{msg.id}",
                user_id=f"{msg.user_id}",
                user_name=sendUser.user_name,
                content=msg.content,
                reactions=newReactions,
                created_time=f"{msg.created_time}",
            )

    async def Subscribe(self, request, context):
        if request.event_id:
            # NOTE: Client has responded that the event has been received,
            # so we can remove it from the queue with the event_id from the
            # request and the user_id from the context

            await event_queue.EventQueue.filter(
                event_id=request.event_id, user_id=context.user_id
            ).delete()

        # NOTE: Broadcast the event to the client
        eventQueue = await event_queue.EventQueue.filter(
            user_id=context.user_id, is_sent=False
        ).all()

        for eventRecord in eventQueue:
            newEvent = await event.Event.get(id=eventRecord.event_id)

            eventRecord.update_from_dict({"is_sent": True})
            await eventRecord.save()

            yield chat_service_pb2.SubscribeResponse(
                event_id=f"{newEvent.id}",
                type=newEvent.type,
                user_id=f"{newEvent.user_id}",
                object_id=f"{newEvent.object_id}",
            )

    async def HealthCheck(self, request, context):
        return chat_service_pb2.HealthCheckResponse(status="ok")
