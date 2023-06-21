from enum import Enum

import typer
from environs import Env

import src.client.app as chatApp

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
    if str(service) == "Service.client":
        chatApp.main()


if __name__ == "__main__":
    typer.run(main)
