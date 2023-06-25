from enum import Enum
from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


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


if TYPE_CHECKING:
    from src.server.internal.auth.entities.user import User

    Event_Pydantic = pydantic_model_creator(Event)
