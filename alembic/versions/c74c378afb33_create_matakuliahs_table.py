"""create matakuliahs table

Revision ID: c74c378afb33
Revises: 
Create Date: 2026-06-23 12:04:58.511843
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'c74c378afb33'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'matakuliah',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('nama', sa.String(length=255), nullable=False),
        sa.Column('kodeMataKuliah', sa.String(length=255), nullable=False),
        sa.Column('isDeleted', sa.Boolean(), nullable=False, default=False),
    )


def downgrade() -> None:
    op.drop_table('matakuliah')
