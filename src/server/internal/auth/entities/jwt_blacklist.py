from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class JWTBlacklist(Model):
    id = fields.UUIDField(pk=True)
    token = fields.CharField(max_length=255)


JWTBlacklist_Pydantic = pydantic_model_creator(JWTBlacklist)
