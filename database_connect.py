import databases as dbs
import sqlalchemy as sa
import os
from dotenv import load_dotenv  
load_dotenv()

POSTGRES_USER = os.environ.get("username", "postgres")
POSTGRES_PASSWORD = os.environ.get("password", "secret")
POSTGRES_DB = os.environ.get("database", "mydatabase")
POSTGRES_HOST = os.environ.get("hostname", "localhost")
POSTGRES_PORT = os.environ.get("port", "5432")

PRODUCTION_ENV = True 
if PRODUCTION_ENV:
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
else:
    DATABASE_URL = os.environ.get("local_database_url",None)

print("Connection URL:", DATABASE_URL)

dbs = dbs.Database(DATABASE_URL)
metadata = sa.MetaData()