import logging

import src.shared.interceptor.base_interceptor as base_interceptor


class LoggingInterceptor(base_interceptor.BaseInterceptor):
    async def intercept(self, method, request, context, method_name):
        logging.info(f"{method_name}")

        return await self.handleRequest(method, request, context)
