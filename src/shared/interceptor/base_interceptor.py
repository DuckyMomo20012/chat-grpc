import grpc
from grpc import ServicerContext
from grpc_interceptor import AsyncServerInterceptor
from grpc_interceptor.exceptions import GrpcException


class BaseInterceptor(AsyncServerInterceptor):
    async def abort_with_unauthenticated(self, context: ServicerContext, message: str):
        await context.abort(grpc.StatusCode.UNAUTHENTICATED, message)

    # Ref: https://grpc-interceptor.readthedocs.io/en/latest/#async-server-interceptors
    async def handleRequest(self, method, request, context):
        try:
            response_or_iterator = method(request, context)
            if not hasattr(response_or_iterator, "__aiter__"):
                # Unary, just await and return the response
                return await response_or_iterator
        except GrpcException as e:
            await context.set_code(e.status_code)
            await context.set_details(e.details)
            raise

        # Server streaming responses, delegate to an async generator helper.
        # Note that we do NOT await this.
        return self._intercept_streaming(response_or_iterator, context)

    # Ref: https://grpc-interceptor.readthedocs.io/en/latest/#async-server-interceptors
    async def _intercept_streaming(self, iterator, context):
        try:
            async for r in iterator:
                yield r
        except GrpcException as e:
            await context.set_code(e.status_code)
            await context.set_details(e.details)
            raise
