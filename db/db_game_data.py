import sqlalchemy as sa
from database_connect import metadata
from utils import generate_uuid
from db.db_enmus import Game, GameLevel


db_game_data = sa.Table(    
    "game_data",
    metadata,
    sa.Column("id", sa.String(36), primary_key=True, default=generate_uuid),
    sa.Column("game_type", sa.Enum(Game), nullable=False),
    sa.Column("question", sa.Text, nullable=False),
    sa.Column("media", sa.Text, nullable=True),
    sa.Column("question_level", sa.Enum(GameLevel), server_default=GameLevel.EASY.name),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
)