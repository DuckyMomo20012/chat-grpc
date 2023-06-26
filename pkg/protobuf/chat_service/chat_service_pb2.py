# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protobuf/chat_service/chat_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,pkg/protobuf/chat_service/chat_service.proto\x12\x07\x63hat.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\'\n\x0bSendRequest\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"0\n\x0fReactionRequest\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\"#\n\x08Reaction\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\xb2\x01\n\x07Message\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12/\n\treactions\x18\x03 \x03(\x0b\x32\x11.chat.v1.ReactionR\treactions\x12=\n\x0c\x63reated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63reatedTime\"3\n\rFetchResponse\x12\"\n\x03msg\x18\x01 \x01(\x0b\x32\x10.chat.v1.MessageR\x03msg\"?\n\x10SubscribeRequest\x12\x1e\n\x08\x65vent_id\x18\x01 \x01(\tH\x00R\x07\x65ventId\x88\x01\x01\x42\x0b\n\t_event_id\"\xbc\x01\n\x11SubscribeResponse\x12\x1e\n\x08\x65vent_id\x18\x01 \x01(\tH\x00R\x07\x65ventId\x88\x01\x01\x12\x17\n\x04type\x18\x02 \x01(\tH\x01R\x04type\x88\x01\x01\x12\x1c\n\x07user_id\x18\x03 \x01(\tH\x02R\x06userId\x88\x01\x01\x12 \n\tobject_id\x18\x04 \x01(\tH\x03R\x08objectId\x88\x01\x01\x42\x0b\n\t_event_idB\x07\n\x05_typeB\n\n\x08_user_idB\x0c\n\n_object_id\"-\n\x13HealthCheckResponse\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status2\xd0\x02\n\x0b\x43hatService\x12\x36\n\x04Send\x12\x14.chat.v1.SendRequest\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x05React\x12\x18.chat.v1.ReactionRequest\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x05\x46\x65tch\x12\x16.google.protobuf.Empty\x1a\x16.chat.v1.FetchResponse\"\x00\x30\x01\x12H\n\tSubscribe\x12\x19.chat.v1.SubscribeRequest\x1a\x1a.chat.v1.SubscribeResponse\"\x00(\x01\x30\x01\x12\x45\n\x0bHealthCheck\x12\x16.google.protobuf.Empty\x1a\x1c.chat.v1.HealthCheckResponse\"\x00\x42\\\n\x0b\x63om.chat.v1B\x10\x43hatServiceProtoP\x01\xa2\x02\x03\x43XX\xaa\x02\x07\x43hat.V1\xca\x02\x07\x43hat\\V1\xe2\x02\x13\x43hat\\V1\\GPBMetadata\xea\x02\x08\x43hat::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protobuf.chat_service.chat_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\013com.chat.v1B\020ChatServiceProtoP\001\242\002\003CXX\252\002\007Chat.V1\312\002\007Chat\\V1\342\002\023Chat\\V1\\GPBMetadata\352\002\010Chat::V1'
  _globals['_SENDREQUEST']._serialized_start=119
  _globals['_SENDREQUEST']._serialized_end=158
  _globals['_REACTIONREQUEST']._serialized_start=160
  _globals['_REACTIONREQUEST']._serialized_end=208
  _globals['_REACTION']._serialized_start=210
  _globals['_REACTION']._serialized_end=245
  _globals['_MESSAGE']._serialized_start=248
  _globals['_MESSAGE']._serialized_end=426
  _globals['_FETCHRESPONSE']._serialized_start=428
  _globals['_FETCHRESPONSE']._serialized_end=479
  _globals['_SUBSCRIBEREQUEST']._serialized_start=481
  _globals['_SUBSCRIBEREQUEST']._serialized_end=544
  _globals['_SUBSCRIBERESPONSE']._serialized_start=547
  _globals['_SUBSCRIBERESPONSE']._serialized_end=735
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=737
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=782
  _globals['_CHATSERVICE']._serialized_start=785
  _globals['_CHATSERVICE']._serialized_end=1121
# @@protoc_insertion_point(module_scope)
