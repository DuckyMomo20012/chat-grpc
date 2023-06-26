from enum import Enum
from typing import TYPE_CHECKING, List, Type

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise.signals import post_save

import src.server.server as server


class EventType(Enum):
    MESSAGE = "MESSAGE"
    REACTION = "REACTION"


class Event(Model):
    id = fields.UUIDField(pk=True)
    type = fields.CharField(max_length=255)
    object_id = fields.UUIDField()

    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="events"
    )
    queues: fields.ReverseRelation["EventQueue"]


if TYPE_CHECKING:
    from src.server.internal.auth.entities.user import User
    from src.server.internal.chat.entities.event_queue import EventQueue

    Event_Pydantic = pydantic_model_creator(Event)


@post_save(Event)
async def event_post_save(
    sender: "Type[Event]",
    instance: Event,
    created: bool,
    using_db,
    update_fields: List[str],
):
    from src.server.internal.chat.entities.event_queue import EventQueue

    for client in server.server.clientPool.clients:
        # NOTE: We already know that the client is authenticated and is a valid
        # user
        await EventQueue.create(event_id=instance.id, user_id=client)
