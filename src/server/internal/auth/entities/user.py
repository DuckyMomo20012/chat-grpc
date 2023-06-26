from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

from src.server.internal.chat.entities.event import Event
from src.server.internal.chat.entities.event_queue import EventQueue
from src.server.internal.chat.entities.message import Message, Reaction


class User(Model):
    id = fields.UUIDField(pk=True)
    user_name = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

    messages = fields.ReverseRelation[Message]
    reactions: fields.ReverseRelation[Reaction]
    events: fields.ReverseRelation[Event]
    queues: fields.ReverseRelation[EventQueue]


User_Pydantic = pydantic_model_creator(User)
