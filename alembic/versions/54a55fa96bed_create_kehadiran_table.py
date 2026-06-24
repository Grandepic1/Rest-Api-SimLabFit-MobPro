"""create kehadiran table

Revision ID: 54a55fa96bed
Revises: b71bf577915d
Create Date: 2026-06-23 21:45:47.892273
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "54a55fa96bed"
down_revision: Union[str, None] = "b71bf577915d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "kehadiran",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("idDosen", sa.Integer(), nullable=False),
        sa.Column("idMataKuliah", sa.Integer(), nullable=False),
        sa.Column("tanggal", sa.Date(), nullable=False),
        sa.Column("jamAwal", sa.Time(), nullable=False),
        sa.Column("jamAkhir", sa.Time(), nullable=False),
        sa.Column("ruangan", sa.String(length=255), nullable=False),
        sa.Column("modul", sa.String(length=255), nullable=False),
        sa.Column("kelas", sa.String(length=255), nullable=False),
        sa.Column("isDeleted", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("googleId", sa.String(length=255), nullable=False),
        sa.Column("photoUrl", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(["idDosen"], ["dosen.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["idMataKuliah"], ["matakuliah.id"], ondelete="CASCADE"),
    )

    op.create_index("ix_kehadiran_idDosen", "kehadiran", ["idDosen"])
    op.create_index("ix_kehadiran_idMataKuliah", "kehadiran", ["idMataKuliah"])


def downgrade() -> None:
    op.drop_index("ix_kehadiran_idMataKuliah", table_name="kehadiran")
    op.drop_index("ix_kehadiran_idDosen", table_name="kehadiran")
    op.drop_table("kehadiran")