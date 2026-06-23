"""create dosenmatakuliah table

Revision ID: b71bf577915d
Revises: 8374d44db496
Create Date: 2026-06-23 12:35:26.812633
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'b71bf577915d'
down_revision: Union[str, None] = '8374d44db496'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dosen_matakuliah",
        sa.Column(
            "dosen_id",
            sa.Integer(),
            sa.ForeignKey("dosen.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "matakuliah_id",
            sa.Integer(),
            sa.ForeignKey("matakuliah.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "dosen_id",
            "matakuliah_id",
            name="pk_dosen_matakuliah",
        ),
    )

    op.create_index(
        "ix_dosen_matakuliah_dosen_id",
        "dosen_matakuliah",
        ["dosen_id"],
    )

    op.create_index(
        "ix_dosen_matakuliah_matakuliah_id",
        "dosen_matakuliah",
        ["matakuliah_id"],
    )


def downgrade() -> None:
    op.drop_index("ix_dosen_matakuliah_matakuliah_id", table_name="dosen_matakuliah")
    op.drop_index("ix_dosen_matakuliah_dosen_id", table_name="dosen_matakuliah")
    op.drop_table("dosen_matakuliah")