import databases as dbs
import sqlalchemy as sa
DATABASE_URL = "postgresql://postgres:123@localhost/curve"

dbs = dbs.Database(DATABASE_URL)
metadata = sa.MetaData()