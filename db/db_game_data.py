import sqlalchemy as sa
from database_connect import metadata
from db.db_enmus import Game, GameLevel


db_game_data = sa.Table(    
    "game_data",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("game_type", sa.Enum(Game), nullable=False),
    sa.Column("question", sa.Text, nullable=False),
    sa.Column("media", sa.Text, nullable=True),
    sa.Column("question_level", sa.Enum(GameLevel), server_default=GameLevel.EASY.name),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
)