<div align="center">

  <h1>Chat gRPC</h1>

  <p>
    Chat app with gRPC Python server
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/DuckyMomo20012/chat-grpc/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/DuckyMomo20012/chat-grpc" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/DuckyMomo20012/chat-grpc" alt="last update" />
  </a>
  <a href="https://github.com/DuckyMomo20012/chat-grpc/network/members">
    <img src="https://img.shields.io/github/forks/DuckyMomo20012/chat-grpc" alt="forks" />
  </a>
  <a href="https://github.com/DuckyMomo20012/chat-grpc/stargazers">
    <img src="https://img.shields.io/github/stars/DuckyMomo20012/chat-grpc" alt="stars" />
  </a>
  <a href="https://github.com/DuckyMomo20012/chat-grpc/issues/">
    <img src="https://img.shields.io/github/issues/DuckyMomo20012/chat-grpc" alt="open issues" />
  </a>
  <a href="https://github.com/DuckyMomo20012/chat-grpc/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/DuckyMomo20012/chat-grpc.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/DuckyMomo20012/chat-grpc/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/chat-grpc">Documentation</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/chat-grpc/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/chat-grpc/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Description](#thought_balloon-description)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Run Locally](#running-run-locally)
    - [Start Manually](#robot-start-manually)
    - [Start with Docker Compose](#whale-start-with-docker-compose)
- [Usage](#eyes-usage)
  - [Generate protobuf](#generate-protobuf)
  - [Application flow](#application-flow)
    - [Server](#server)
      - [Server initialization](#server-initialization)
      - [Authentication](#authentication)
      - [Message broadcasting](#message-broadcasting)
      - [Logging](#logging)
    - [Client](#client)
      - [Client initialization](#client-initialization)
      - [Authentication](#authentication)
      - [Event listener](#event-listener)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  - [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->

## :star2: About the Project

<!-- Description -->

### :thought_balloon: Description:

- Each user can send messages to other users, only if the previous message sent
  by the user has been reacted by **two** other users. If not, the message will
  be rejected.

- Each user can react to messages sent by other users, and by the user itself.
  However, the self reaction will not be counted to the message when checking if
  the message can be sent to other users.

<!-- Screenshots -->

### :camera: Screenshots

<div align="center">
  <img src="https://github.com/DuckyMomo20012/chat-grpc/assets/64480713/043a0ec1-00c8-47a8-b232-8d1243fd86f8" alt="screenshot" />
  <i>Last updated: Jun 29, 2023</i>
</div>

<div align="center">
  <img src="https://github.com/DuckyMomo20012/chat-grpc/assets/64480713/54dc0736-67e0-42ec-a3db-3a92e3fc20e9" alt="screenshot_1" />
  <i>Last updated: Jun 29, 2023</i>
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://grpc.io/">gRPC</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://grpc.io/">gRPC</a></li>
    <li><a href="https://tortoise.github.io/">Tortoise ORM</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<!-- Features -->

### :dart: Features

- Basic authentication.
- Chat with other users.
- React to messages.

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to
your `.env` file:

- **Server configs:**

  `PORT`: Port to run the server.

  `JWT_SECRET_KEY`: Secret key to sign JWT tokens.

  `JWT_EXPIRATION_TIME`: Expiration time of JWT tokens, **in seconds** . Default
  is `3600` seconds.

  `DB_CONNECTION_STRING`: Postgres connection string to connect to the database.

- **Client configs:**

  `PORT`: Port to run the server.

  `SERVER_HOST`: Host of the server.

E.g:

```
# .env
PORT="9000"
JWT_SECRET_KEY="secret"
JWT_EXPIRATION_TIME="3600"
DB_CONNECTION_STRING="postgres://postgres:postgres@localhost:5432/chat"

SERVER_HOST="localhost"
```

You can also check out the file `.env.example` to see all required environment
variables.

<!-- Getting Started -->

## :toolbox: Getting Started

<!-- Prerequisites -->

### :bangbang: Prerequisites

- Python: `>= 3.11`.

- This project uses [Poetry](https://python-poetry.org/) as package manager:

  Linux, macOS, Windows (WSL)

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

  Read more about installation on
  [Poetry documentation](https://python-poetry.org/docs/master/#installation).

<!-- Run Locally -->

### :running: Run Locally

Clone the project:

```bash
git clone https://github.com/DuckyMomo20012/chat-grpc.git
```

Go to the project directory:

```bash
cd chat-grpc
```

Install dependencies:

```bash
poetry install
```

OR:

Install dependencies with `pip`:

```bash
pip install -r requirements.txt
```

<details>
<summary>Export dependencies from </code>pyproject.toml</code></summary>

Export Poetry dependencies to file `requirements.txt`:

```bash
poetry export -f requirements.txt --output requirements.txt
```

> **Note**: You can add option: `--dev` to include development dependencies.

</details>

<!-- Start Manually -->

#### :robot: Start Manually

- Setup database:

  ```bash
  make compose-db
  ```

- Start the server:

  - Activate the virtual environment:

    ```bash
    poetry shell
    ```

  - Start the server:

    ```bash
    poe dev
    ```

- Stop the database:

  ```bash
  make compose-down
  ```

- Start the client:

  - Activate the virtual environment:

    ```bash
    poetry shell
    ```

  - Start the client:

    ```bash
    poe dev client
    ```

<!-- Start with Docker Compose -->

#### :whale: Start with Docker Compose

Start the server and database:

```bash
make compose-up
```

Stop the server and database:

```bash
make compose-down
```

<!-- Usage -->

## :eyes: Usage

### Generate protobuf

```bash
make gen-proto
```

This will generate the protobuf files in the `chat_grpc/proto` directory using
the file `buf.gen.yaml` as configuration.

<details>
<summary>The auto-generated file problem</summary>

Due to the problem with the auto-generated python absolute imports in the files
`.*_pb2_gprc.py`, you **HAVE TO nested** the proto directory in the `proto`
directory.

For example:

- If you move configure the `proto` directory with the
  `proto/auth_service/auth_service.proto` or
  `proto/chat_service/chat_service.proto`
- Configure the `buf.gen.yaml` file with the `out` configure to
  `../pkg/protobuf`.
- Then the auto-generated files will be in the `pkg/protobuf` directory, just
  like current configuration. However, the file `.*_pb2_gprc.py` will have the
  import `from auth_service ...` instead of
  `from pkg.protobuf.chat_service ...`.

</details>

### Makefile

- `make gen-proto`: Generate protobuf files.

  Usage:

  ```bash
  make gen-proto
  ```

- `make server`: Start the server.

  Usage:

  ```bash
  make server
  ```

- `make client`: Start the client.

  Usage:

  ```bash
  make client
  ```

- `make compose-up`: Start the server and database with docker compose.

  Usage:

  ```bash
  make compose-up
  ```

- `make compose-down`: Stop the server and database with docker compose.

  Usage:

  ```bash
  make compose-down
  ```

- `make compose-db`: Start the database with docker compose (without the
  server).

  Usage:

  ```bash
  make compose-db
  ```

### CLI

```bash
$ python cli.py --help

Usage: cli.py [OPTIONS] [SERVICE]:[server|client]

Arguments:
  [SERVICE]:[server|client]  Service to run  [default: server]

Options:
  --help  Show this message and exit.
```

> **Note**: This is an entry point for all the services. Each service should be
> run from this entry point to make the absolute import work.

### Application flow

#### Server

##### Server initialization

First, the server is configured with **interceptors** to handle authentication
and logging. The gRPC server is registered with two main services: `AuthService`
and `ChatService`. Finally, the server is listening on the address `[::]:PORT`,
with `PORT` is the environment variable.

Then, the server also init the Tortoise ORM to connect to the database. The
tortoise ORM is configured with the environment variable `DB_CONNECTION_STRING`.
This library also automatically generate the database schema for the models,
which are configured by specifying the `models` file paths while initializing
the ORM.

The server also create a `Server` object to hold the `set` of connected clients.
While updating this set of clients, the server will use an `asyncio.Lock` to
prevent concurrent access.

##### Authentication

Each client will have a **token** to authenticate with the server. The token is
generated by the server when the client login. The token is a JWT token, which
holds the `user_id` and `user_name` of the user, and the `exp` time. The token
is signed with the `secret` key, which is configured by the environment variable
`JWT_SECRET_KEY`. The token is valid for **1 hour**, which is configured by the
`JWT_EXPIRE_TIME` environment variable.

The JWT interceptor will check the token in the metadata of the request. If the
token is valid, the request will be passed to the next interceptor. Otherwise,
the interceptor will return an error to the client. The interceptor will ignore
the authentication for the `login` and `register` methods. Also, the interceptor
will **"inject" the `user_id` into the context** of the request.

After the user logged in, the server will add the `user_id` to the `Server`
**set** of connected clients.

After the user signed out, the token will be revoked by putting into the
**blacklist table**. The JWT interceptor will check the token in the blacklist
table. If the token is in the blacklist table, the interceptor will return an
error to the client.

> **Note**: Currently, the blacklist table has to be manually cleaned up.

##### Message broadcasting

Every time a client sends a message or reacts to a message, the server will
create an `Event` record in the database. The `Event` record will be used to
store history of the chat conversation. After the `Event` record is created, the
`pre_save` hook will be called to create another `EventQueue` record. The number
of `EventQueue` records is equal to the number of connected clients, which is
stored as a `set` in the `Server` object. The `EventQueue` record will be used
to broadcast the message to the clients.

The `EventQueue` record is send back to the client as a `Subscribe` route
response, and the record will be marked as sent by setting the `is_sent` field
to `True`. The client will use the `Subscribe` route to receive the `EventQueue`
and then send back the `message_id` back to the server to **acknowledge** that
it has received the event queue. The server will then delete the `EventQueue`
record from the database that matches the `message_id`.

If the client is logged in, but close the app without logging out, the server
will also send the `EventQueue` record to the client when it connects again, as
the `user_id` is still in the `Server` set of connected clients.

> **Note**: Sometimes, the client receives the `EventQueue` record, but the
> client don't send back the `message_id` to the server. This will cause the
> database to have a lot of `EventQueue` records that are not deleted. This
> problem is not solved yet, and the `EventQueue` records have to be manually be
> deleted.

##### Logging

The server will log the request and response of each route by the logging
interceptor. The log is visible in the console, and also in the `logs`
directory.

#### Client

##### Client initialization

The client is built with the `DearPyGui` library. The client will connect to the
server with the address `[::]:PORT`, with `PORT` is the environment variable.

##### Authentication

The client will send the `login` request to the server with the `user_name` and
the `password`. The server will return the `access_token` and this is stored in
the `Client` object. The `access_token` is used to authenticate with the server.

When the client sends the request to the server, the `access_token` is added to
the metadata of the request (as the `Bearer` authorization token), by the token
interceptor.

After the client logged out, the access token will be deleted from the client.

> **Note**: Currently, the client will not automatically refresh the token.

##### Event listener

After login successfully, the client starts a **deamon thread** to send the
`Subscribe` request to the server to receive the `EventQueue` record, within the
loop. The client will send back to the server the `message_id` of the
`EventQueue` record that it has just received.

<!-- Roadmap -->

## :compass: Roadmap

- [x] Hash passwords.
- [ ] Notification panel.
- [ ] Refresh token to keep user logged in.
- [ ] Improve ORM queries.
- [ ] Improve error handling.

<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/DuckyMomo20012/chat-grpc/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DuckyMomo20012/chat-grpc" />
</a>

Contributions are always welcome!

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the
[Code of Conduct](https://github.com/DuckyMomo20012/chat-grpc/blob/main/CODE_OF_CONDUCT.md).

<!-- FAQ -->

## :grey_question: FAQ

- The client app is not responding when closing the app.

  - This is because the client still has working thread. Maybe, the client has
    some errors, which causes the thread to not stop. You can try to close the
    app again, or kill the app process, or **just spam the Ctrl+C**.

- Cannot handle errors in event listener which run in a thread.

  - Handle errors in thread is quite difficult. I will look into this later.
    Currently, I can only handle the errors in the callback function of the
    event listener.

<!-- License -->

## :warning: License

Distributed under MIT license. See
[LICENSE](https://github.com/DuckyMomo20012/chat-grpc/blob/main/LICENSE) for
more information.

<!-- Contact -->

## :handshake: Contact

Duong Vinh - [@duckymomo20012](https://twitter.com/duckymomo20012) -
tienvinh.duong4@gmail.com

Project Link:
[https://github.com/DuckyMomo20012/chat-grpc](https://github.com/DuckyMomo20012/chat-grpc).

<!-- Acknowledgments -->

## :gem: Acknowledgements

Here are useful resources and libraries that we have used in our projects:

- [Buf CLI](https://buf.build/product/cli/): Generate code, prevent breaking
  changes, lint Protobuf schemas, enforce best practices, and invoke APIs with
  the Buf CLI.
- [grpc-interceptor](https://grpc-interceptor.readthedocs.io/en/latest/):
  Simplified Python gRPC Interceptors.
- [Dear PyGui](https://dearpygui.readthedocs.io/en/latest/): Dear PyGui is an
  easy-to-use, dynamic, GPU-Accelerated, cross-platform graphical user interface
  toolkit(GUI) for Python. It is “built with”
  [Dear ImGui](https://github.com/ocornut/imgui).
