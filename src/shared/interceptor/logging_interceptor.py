import logging

import src.shared.interceptor.base_interceptor as base_interceptor

ignoreEndpoints = ["/chat.v1.ChatService/Subscribe"]


class LoggingInterceptor(base_interceptor.BaseInterceptor):
    async def intercept(self, method, request, context, method_name):
        if method_name in ignoreEndpoints:
            return await self.handleRequest(method, request, context)

        logging.info(f"{method_name}")

        return await self.handleRequest(method, request, context)
