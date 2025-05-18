import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

api = FastAPI()

connectionString = os.getenv('CONNECTION_STRING')
conn = psycopg2.connect(connectionString)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()


@api.get("/")
def read_root():
    return {"Hello": "World"}