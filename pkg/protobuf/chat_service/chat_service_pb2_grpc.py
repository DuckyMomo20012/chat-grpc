# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pkg.protobuf.chat_service import chat_service_pb2 as pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Send = channel.unary_unary(
                '/chat.v1.ChatService/Send',
                request_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SendRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.React = channel.unary_unary(
                '/chat.v1.ChatService/React',
                request_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.ReactionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Fetch = channel.unary_stream(
                '/chat.v1.ChatService/Fetch',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.Message.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/chat.v1.ChatService/Subscribe',
                request_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeResponse.FromString,
                )
        self.HealthCheck = channel.unary_unary(
                '/chat.v1.ChatService/HealthCheck',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.HealthCheckResponse.FromString,
                )


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Send(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def React(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Send': grpc.unary_unary_rpc_method_handler(
                    servicer.Send,
                    request_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SendRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'React': grpc.unary_unary_rpc_method_handler(
                    servicer.React,
                    request_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.ReactionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Fetch': grpc.unary_stream_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.Message.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeRequest.FromString,
                    response_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeResponse.SerializeToString,
            ),
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.v1.ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Send(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.v1.ChatService/Send',
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SendRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def React(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.v1.ChatService/React',
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.ReactionRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/chat.v1.ChatService/Fetch',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/chat.v1.ChatService/Subscribe',
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeRequest.SerializeToString,
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.v1.ChatService/HealthCheck',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pkg_dot_protobuf_dot_chat__service_dot_chat__service__pb2.HealthCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
