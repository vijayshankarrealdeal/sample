import sqlalchemy as sa
from db.db_enmus import GameLevel, UserType
from database_connect import metadata
from utils import generate_uuid

db_user_table = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.String(225), primary_key=True),
    sa.Column("email", sa.String(255), nullable=False, unique=True),
    sa.Column("user_type", sa.Enum(UserType), nullable=False,server_default=UserType.USER.name),
    sa.Column("password", sa.String(255), nullable=False),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    sa.Column('game_level',sa.Enum(GameLevel),server_default=GameLevel.EASY.name)
)
