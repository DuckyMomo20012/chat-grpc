from typing import Any, Callable

import grpc
from grpc_interceptor import ClientCallDetails, ClientInterceptor

import src.client.app as app


# Ref: https://grpc-interceptor.readthedocs.io/en/latest/#client-interceptors
class TokenInterceptor(ClientInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        if app.app.accessToken:
            accessToken = app.app.accessToken

            new_details = ClientCallDetails(
                call_details.method,
                call_details.timeout,
                [("authorization", f"Bearer {accessToken}")],
                call_details.credentials,
                call_details.wait_for_ready,
                call_details.compression,
            )

            return method(request_or_iterator, new_details)

        return method(request_or_iterator, call_details)
