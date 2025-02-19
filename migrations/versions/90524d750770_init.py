"""init

Revision ID: 90524d750770
Revises: 
Create Date: 2025-02-19 17:42:06.542242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90524d750770'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import text

# Define ENUM types
game_enum = ENUM('CARDS', 'TRUTH_DARE', 'BOARD_GAME', 'SCRATCH', name='game', create_type=False)
game_level_enum = ENUM('EASY', 'MEDIUM', 'HARD', 'INTENSE', 'SUPER', name='gamelevel', create_type=False)
user_type_enum = ENUM('ADMIN', 'USER', name='usertype', create_type=False)

def upgrade() -> None:
    bind = op.get_bind()

    # ✅ FIX: Use sa.text() when executing raw SQL
    existing_game_enum = bind.execute(text("SELECT typname FROM pg_type WHERE typname = 'game'")).fetchall()
    if not existing_game_enum:
        game_enum.create(bind)

    existing_gamelevel_enum = bind.execute(text("SELECT typname FROM pg_type WHERE typname = 'gamelevel'")).fetchall()
    if not existing_gamelevel_enum:
        game_level_enum.create(bind)

    existing_usertype_enum = bind.execute(text("SELECT typname FROM pg_type WHERE typname = 'usertype'")).fetchall()
    if not existing_usertype_enum:
        user_type_enum.create(bind)

    # Create `game_data` table
    op.create_table('game_data',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('game_type', game_enum, nullable=False),
        sa.Column('question', sa.Text(), nullable=False),
        sa.Column('media', sa.Text(), nullable=True),
        sa.Column('question_level', game_level_enum, server_default='EASY', nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create `users` table
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('user_type', user_type_enum, server_default='USER', nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('game_level', game_level_enum, server_default='EASY', nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade() -> None:
    # Drop tables first
    op.drop_table('game_data')
    op.drop_table('users')

    # Drop ENUM types if no longer in use
    op.execute(text("DROP TYPE IF EXISTS game CASCADE"))
    op.execute(text("DROP TYPE IF EXISTS gamelevel CASCADE"))
    op.execute(text("DROP TYPE IF EXISTS usertype CASCADE"))

