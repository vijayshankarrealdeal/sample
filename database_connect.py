import databases as dbs
import sqlalchemy as sa
import os

POSTGRES_USER = os.environ.get("username", "postgres")
POSTGRES_PASSWORD = os.environ.get("password", "secret")
POSTGRES_DB = os.environ.get("database", "mydatabase")
POSTGRES_HOST = os.environ.get("hostname", "localhost")
POSTGRES_PORT = os.environ.get("port", "5432")

PRODUCTION_ENV = True
if PRODUCTION_ENV:
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}_test"
    )
else:
    DATABASE_URL = "postgresql://curve_admin:nWr82461QEBFOTtu11bboYnEzgb99gjY@dpg-cuqs2a52ng1s73fa97bg-a.oregon-postgres.render.com/curves"

print("Connection URL:", DATABASE_URL)

dbs = dbs.Database(DATABASE_URL)
metadata = sa.MetaData()