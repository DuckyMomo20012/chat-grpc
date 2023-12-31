from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Message(Model):
    id = fields.UUIDField(pk=True)
    content = fields.TextField()
    #: The date-time the Message record was created at
    created_time = fields.DatetimeField(auto_now_add=True)

    # NOTE: Don't use `user_id` as the field name, because Tortoise ORM will
    # append `_id` to the field name
    # Ref: https://tortoise.github.io/models.html#the-db-backing-field
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="messages"
    )
    reactions = fields.ReverseRelation["Reaction"]


class Reaction(Model):
    id = fields.UUIDField(pk=True)

    message: fields.ForeignKeyRelation["Message"] = fields.ForeignKeyField(
        "models.Message", related_name="reactions"
    )
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="reactions"
    )


if TYPE_CHECKING:
    from src.server.internal.auth.entities.user import User

    Message_Pydantic = pydantic_model_creator(Message)
    Reaction_Pydantic = pydantic_model_creator(Reaction)
