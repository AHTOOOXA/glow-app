"""friendships

Revision ID: 4d4d0dbf3c31
Revises: f8d34589dbe1
Create Date: 2024-10-21 21:05:57.912923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4d4d0dbf3c31'
down_revision: Union[str, None] = 'f8d34589dbe1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quizresponses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('taker_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['taker_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quizresponses')
    # ### end Alembic commands ###