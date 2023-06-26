from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class EventQueue(Model):
    id = fields.UUIDField(pk=True)
    is_sent = fields.BooleanField(default=False)

    event: fields.ForeignKeyRelation["Event"] = fields.ForeignKeyField(
        "models.Event", related_name="queues"
    )
    # NOTE: Target client to broadcast the event to
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="queues"
    )


if TYPE_CHECKING:
    from src.server.internal.auth.entities.user import User
    from src.server.internal.chat.entities.event import Event

    EventQueue_Pydantic = pydantic_model_creator(EventQueue)
