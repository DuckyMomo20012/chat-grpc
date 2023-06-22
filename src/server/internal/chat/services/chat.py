import pkg.protobuf.chat_service.chat_service_pb2 as chat_service_pb2
import pkg.protobuf.chat_service.chat_service_pb2_grpc as chat_service_pb2_grpc


class ChatService(chat_service_pb2_grpc.ChatServiceServicer):
    def HealthCheck(self, request, context):
        return chat_service_pb2.HealthCheckResponse(status="ok")
