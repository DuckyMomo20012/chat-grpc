from environs import Env

env = Env()
# Read .env into os.environ
env.read_env()

print("Hello World")

TEST_VAR = env.str("TEST_VAR", "Not set")

print(f"My secret key: {TEST_VAR}")
