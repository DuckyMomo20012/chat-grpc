from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

from src.server.internal.chat.entities.message import Message, Reaction


class User(Model):
    id = fields.IntField(pk=True)
    user_name = fields.CharField(max_length=255)

    messages = fields.ReverseRelation[Message]
    reactions: fields.ReverseRelation[Reaction]


User_Pydantic = pydantic_model_creator(User)
