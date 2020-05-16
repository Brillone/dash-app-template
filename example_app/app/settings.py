import os
from dotenv import load_dotenv
import json

# internal
from app_logging import initialize_logger

# load env
load_dotenv('utils/.env')

# load env
_env_mode = os.getenv('APP_ENV')

# load env variables
_app_name = os.getenv('APP_NAME')
_app_host = os.getenv('APP_HOST')
_app_port = int(os.getenv('APP_PORT'))
_mssql_user = os.getenv('MSSQL_USER')
_mssql_password = os.getenv('MSSQL_PASSWORD')
_slack_token = os.getenv('SLACK_TOKEN')
_app_user = os.getenv('APP_USER')
_app_password = os.getenv('APP_PASSWORD')

env_variables = {'app_name': _app_name,
                 'env_mode': _env_mode,
                 'app_host': _app_host, 'app_port': _app_port,
                 'mssql_user': _mssql_user,
                 'mssql_password': _mssql_password,
                 'app_user': _app_user,
                 'app_password': _app_password}

with open('utils/config.json', 'r') as fp:
    writer_config = json.load(fp)[_env_mode]['writer_config']

with open('utils/config.json', 'r') as fp:
    scheduler_config = json.load(fp)[_env_mode]['scheduler_config']

# logger
logger = initialize_logger('logs/', env_variables['app_name'])
