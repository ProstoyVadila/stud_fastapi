import os

from dotenv import load_dotenv


load_dotenv()

PG_DATABASE = os.getenv('PG_DATABASE')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
HOST = os.getenv('HOST')
POST = os.getenv('PORT')
