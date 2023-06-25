import grpc
from google.protobuf.timestamp_pb2 import Timestamp

import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc
import src.server.internal.chat.entities.event as event
import src.server.internal.chat.entities.message as message


class ChatService(chat_service_pb2_grpc.ChatServiceServicer):
    async def Send(self, request, context):
        userId = context.user_id

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

    async def Fetch(self, request, context):
        messages = await message.Message.all()

        for msg in messages:
            newCreatedTime = Timestamp()
            newCreatedTime.FromDatetime(msg.created_time)

            reactions = await msg.reactions.all()

            newReactions = []
            for reaction in reactions:
                newReactions.append(
                    chat_service_pb2.Reaction(
                        user_id=f"{reaction.user_id}",
                    )
                )

            yield chat_service_pb2.FetchResponse(
                msg=chat_service_pb2.Message(
                    message_id=f"{msg.id}",
                    content=msg.content,
                    created_time=newCreatedTime,
                    reactions=newReactions,
                )
            )

    async def HealthCheck(self, request, context):
        return chat_service_pb2.HealthCheckResponse(status="ok")
