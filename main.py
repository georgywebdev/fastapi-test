import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

api = FastAPI()

url = os.getenv('DATABASE_URL')
connection = psycopg2.connect(url)


@api.get("/")
def read_root():
    return {"Hello": "World"}