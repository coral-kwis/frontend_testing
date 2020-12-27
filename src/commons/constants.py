import os
# Reads the key-value pair from .env file and adds them to environment variable.
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# ENV VARIABLES
ENV = os.getenv('ENV', 'test')
ADMIN_USER = os.getenv('ADMIN_USER')
ADMIN_PWD = os.getenv('ADMIN_PWD')

# PATH
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
USERS_FILE_PATH = os.path.join(ROOT_DIR, 'data', 'users.xlsx')
CONFIG_PATH = os.path.join(ROOT_DIR, 'configs', 'hosts_config.json')

# CONSTANTS VARIABLES
TIMEOUT = 30
SHORT_TIMEOUT = 10
