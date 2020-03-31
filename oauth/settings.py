import environ

# for running local without docker
# environ.Env.read_env()
# env_file = (environ.Path(__file__) - 2) + ".env"
# environ.Env.read_env(str(env_file))

env = environ.Env()

# DATABASE
DATABASE_DRIVER = env('DATABASE_DRIVER')
DATABASE_HOST = env('DATABASE_HOST')
DATABASE_USERNAME = env('DATABASE_USERNAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_NAME = env('DATABASE_NAME')

database_url_str = "mysql://root:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}:3306/{DATABASE}"
DATABASE_URL = database_url_str.format(MYSQL_ROOT_PASSWORD=DATABASE_PASSWORD, MYSQL_HOST=DATABASE_HOST,
                                       DATABASE=DATABASE_NAME)

# DECRYPTION
DECRYPTION_IV = env('DECRYPTION_IV')
DECRYPTION_KEY = env('DECRYPTION_KEY')

# Cache
REDIS_SERVER_PORT = env('REDIS_SERVER_PORT')
REDIS_SERVER_HOST = env('REDIS_SERVER_HOST')
