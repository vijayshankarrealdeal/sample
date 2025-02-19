from database_connect import dbs
import sqlalchemy as sa
from db.db_learn_data import article_db_table, section_db_table


async def get_articles():
    stm = sa.select(article_db_table)
    query = await dbs.fetch_all(stm)
    return query

async def get_sections(article_id):
    stm = sa.select(section_db_table).where(section_db_table.c.article_id == article_id)
    query = await dbs.fetch_all(stm)
    return query