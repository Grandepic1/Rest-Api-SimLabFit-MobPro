"""create dosen table

Revision ID: 8374d44db496
Revises: c74c378afb33
Create Date: 2026-06-23 12:25:30.862600
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = '8374d44db496'
down_revision: Union[str, None] = 'c74c378afb33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dosen",
        sa.Column('id', sa.Integer, nullable=False, primary_key=True, autoincrement=True),
        sa.Column('nama', sa.String(255), nullable=False),
        sa.Column('kodeDosen', sa.String(255), nullable=False),
        sa.Column('isDeleted', sa.Boolean, default=False, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('dosen')
