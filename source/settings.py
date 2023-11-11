import os

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv('DB_PATH')
HEX_ENCODE_KEY = os.getenv('HEX_ENCODE_KEY')


