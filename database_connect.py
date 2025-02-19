import databases as dbs
import sqlalchemy as sa
import os

POSTGRES_USER = os.environ.get("username", "postgres")
POSTGRES_PASSWORD = os.environ.get("password", "secret")
POSTGRES_DB = os.environ.get("database", "mydatabase")
POSTGRES_HOST = os.environ.get("hostname", "localhost")
POSTGRES_PORT = os.environ.get("port", "5432")

# Construct the connection URL
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

print("Connection URL:", DATABASE_URL)

dbs = dbs.Database(DATABASE_URL)
metadata = sa.MetaData()