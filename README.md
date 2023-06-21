<div align="center">

  <h1>Python Template</h1>

  <p>
    A simple Python template
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/DuckyMomo20012/python-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/DuckyMomo20012/python-template" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/DuckyMomo20012/python-template" alt="last update" />
  </a>
  <a href="https://github.com/DuckyMomo20012/python-template/network/members">
    <img src="https://img.shields.io/github/forks/DuckyMomo20012/python-template" alt="forks" />
  </a>
  <a href="https://github.com/DuckyMomo20012/python-template/stargazers">
    <img src="https://img.shields.io/github/stars/DuckyMomo20012/python-template" alt="stars" />
  </a>
  <a href="https://github.com/DuckyMomo20012/python-template/issues/">
    <img src="https://img.shields.io/github/issues/DuckyMomo20012/python-template" alt="open issues" />
  </a>
  <a href="https://github.com/DuckyMomo20012/python-template/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/DuckyMomo20012/python-template.svg" alt="license" />
  </a>
</p>

<h4>
    <a href="https://github.com/DuckyMomo20012/python-template/">View Demo</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/python-template">Documentation</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/python-template/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/DuckyMomo20012/python-template/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  - [Screenshots](#camera-screenshots)
  - [Tech Stack](#space_invader-tech-stack)
  - [Features](#dart-features)
  - [Color Reference](#art-color-reference)
  - [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  - [Prerequisites](#bangbang-prerequisites)
  - [Run Locally](#running-run-locally)
  - [Running Tests](#test_tube-running-tests)
  - [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  - [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

<!-- About the Project -->

## :star2: About the Project

<!-- Screenshots -->

### :camera: Screenshots

<div align="center">
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>

<!-- TechStack -->

### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://expressjs.com/">Express.js</a></li>
    <li><a href="https://go.dev/">Golang</a></li>
    <li><a href="https://nestjs.com/">Nest.js</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>
    <li><a href="https://www.prisma.io/">Prisma</a></li>
    <li><a href="https://www.apollographql.com/">Apollo</a></li>
    <li><a href="https://graphql.org/">GraphQL</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
    <li><a href="https://neo4j.com/">Neo4j</a></li>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://www.jenkins.io/">Jenkins</a></li>
    <li><a href="https://circleci.com/">CircleCLI</a></li>
  </ul>
</details>

<!-- Features -->

### :dart: Features

- Feature 1.
- Feature 2.
- Feature 3.

<!-- Color Reference -->

### :art: Color Reference

| Color           | Hex                                                              |
| --------------- | ---------------------------------------------------------------- |
| Primary Color   | ![#222831](https://placehold.jp/222831/222831/10x10.png) #222831 |
| Secondary Color | ![#393E46](https://placehold.jp/393E46/393E46/10x10.png) #393E46 |
| Accent Color    | ![#00ADB5](https://placehold.jp/00ADB5/00ADB5/10x10.png) #00ADB5 |
| Text Color      | ![#EEEEEE](https://placehold.jp/EEEEEE/EEEEEE/10x10.png) #EEEEEE |

<!-- Env Variables -->

### :key: Environment Variables

To run this project, you will need to add the following environment variables to
your `.env` file:

- **App configs:**

  `TEST_VAR`: Description of this environment variable.

E.g:

```
# .env
TEST_VAR="my secret key"
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
git clone https://github.com/DuckyMomo20012/python-template.git
```

Go to the project directory:

```bash
cd python-template
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

---

Activate the virtual environment:

```bash
poetry shell
```

Start the program:

```bash
poe dev
```

<!-- Running Tests -->

### :test_tube: Running Tests

To run tests, run the following command:

```bash
poe test
```

<!-- Deployment -->

### :triangular_flag_on_post: Deployment

To deploy this project run:

```bash
poe deploy
```

<!-- Usage -->

## :eyes: Usage

Use this space to tell a little more about your project and how it can be used.
Show additional screenshots, code samples, demos, or links to other resources.

```python
from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

print("Hello World")

TEST_VAR = env.str("TEST_VAR")

print(f"My secret key: {TEST_VAR}")
```

<!-- Roadmap -->

## :compass: Roadmap

- [x] Todo 1.
- [ ] Todo 2.

<!-- Contributing -->

## :wave: Contributing

<a href="https://github.com/DuckyMomo20012/python-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DuckyMomo20012/python-template" />
</a>

Contributions are always welcome!

<!-- Code of Conduct -->

### :scroll: Code of Conduct

Please read the
[Code of Conduct](https://github.com/DuckyMomo20012/python-template/blob/main/CODE_OF_CONDUCT.md).

<!-- FAQ -->

## :grey_question: FAQ

- Question 1

  - Answer 1.

- Question 2

  - Answer 2.

<!-- License -->

## :warning: License

Distributed under MIT license. See
[LICENSE](https://github.com/DuckyMomo20012/python-template/blob/main/LICENSE)
for more information.

<!-- Contact -->

## :handshake: Contact

Duong Vinh - [@duckymomo20012](https://twitter.com/duckymomo20012) -
tienvinh.duong4@gmail.com

Project Link:
[https://github.com/DuckyMomo20012/python-template](https://github.com/DuckyMomo20012/python-template).

<!-- Acknowledgments -->

## :gem: Acknowledgements

Here are useful resources and libraries that we have used in our projects:

- [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template):
  A detailed template to bootstrap your README file quickly.
