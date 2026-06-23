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
            "idDosen",
            sa.Integer(),
            sa.ForeignKey("dosen.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "idMataKuliah",
            sa.Integer(),
            sa.ForeignKey("matakuliah.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "idDosen",
            "idMataKuliah",
            name="pk_dosen_matakuliah",
        ),
    )

    op.create_index(
        "ix_dosen_matakuliah_idDosen",
        "dosen_matakuliah",
        ["idDosen"],
    )

    op.create_index(
        "ix_dosen_matakuliah_idMataKuliah",
        "dosen_matakuliah",
        ["idMataKuliah"],
    )


def downgrade() -> None:
    op.drop_index("ix_dosen_matakuliah_idMataKuliah", table_name="dosen_matakuliah")
    op.drop_index("ix_dosen_matakuliah_idDosen", table_name="dosen_matakuliah")
    op.drop_table("dosen_matakuliah")