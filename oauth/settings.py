import environ

# for running local without docker
environ.Env.read_env()
env_file = (environ.Path(__file__) - 2) + ".env"
environ.Env.read_env(str(env_file))

env = environ.Env()

# DATABASE
DATABASE_DRIVER = env('DATABASE_DRIVER')
DATABASE_HOST = env('DATABASE_HOST')
DATABASE_USERNAME = env('DATABASE_USERNAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_NAME = env('DATABASE_NAME')

# DECRYPTION
DECRYPTION_IV = env('DECRYPTION_IV')
DECRYPTION_KEY = env('DECRYPTION_KEY')
