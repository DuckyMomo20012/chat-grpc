from enum import Enum

import typer
from environs import Env

TService = Enum(  # type: ignore
    "Service",
    {
        k: k
        for k in [
            "server",
            "client",
        ]
    },
)

env = Env()
# Read .env into os.environ
env.read_env()


def main(service: TService = typer.Argument("server", help="Service to run")):
    if str(service) == "Service.server":
        import src.server.server as server

        server.main()
    elif str(service) == "Service.client":
        import src.client.app as chatApp

        chatApp.main()


if __name__ == "__main__":
    typer.run(main)
