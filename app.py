import logging, os

from os.path import join, dirname
from dotenv import load_dotenv

from api import init_api

## Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

## Get config
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KEY = os.environ.get("FLASK_KEY")
JWT_KEY = os.environ.get("JWT_KEY")

app_api = init_api(KEY, JWT_KEY)
