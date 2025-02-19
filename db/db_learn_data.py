import sqlalchemy as sa
from database_connect import metadata

article_db_table = sa.Table(
    'article',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.Text, nullable=False),
    sa.Column('introduction', sa.Text, nullable=False),
    sa.Column('conclusion', sa.Text, nullable=False),
    sa.Column('sections_count', sa.Integer, nullable=True),
    sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now()),
)


section_db_table = sa.Table(
    'section',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('heading', sa.Text, nullable=False),
    sa.Column('content', sa.Text, nullable=False),
    sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now()),
    sa.Column('article_id', sa.Integer, sa.ForeignKey('article.id'))
)
