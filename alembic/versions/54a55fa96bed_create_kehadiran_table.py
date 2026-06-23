"""create kehadiran table

Revision ID: 54a55fa96bed
Revises: b71bf577915d
Create Date: 2026-06-23 21:45:47.892273
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = '54a55fa96bed'
down_revision: Union[str, None] = 'b71bf577915d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "kehadiran",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("id_dosen", sa.Integer(), nullable=False),
        sa.Column("id_matakuliah", sa.Integer(), nullable=False),

        # tidak memakai String
        sa.Column("tanggal", sa.Date(), nullable=False),
        sa.Column("jam_awal", sa.Time(), nullable=False),
        sa.Column("jam_akhir", sa.Time(), nullable=False),

        sa.Column("ruangan", sa.String(length=255), nullable=False),
        sa.Column("modul", sa.String(length=255), nullable=False),
        sa.Column("kelas", sa.String(length=255), nullable=False),
        sa.Column("user_google_id", sa.String(length=255), nullable=False),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        ),

        sa.ForeignKeyConstraint(
            ["id_dosen"],
            ["dosen.id"],
            ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["id_matakuliah"],
            ["matakuliah.id"],
            ondelete="CASCADE"
        ),
    )

    op.create_index(
        "ix_kehadiran_id_dosen",
        "kehadiran",
        ["id_dosen"]
    )

    op.create_index(
        "ix_kehadiran_id_matakuliah",
        "kehadiran",
        ["id_matakuliah"]
    )


def downgrade():
    op.drop_index("ix_kehadiran_id_matakuliah", table_name="kehadiran")
    op.drop_index("ix_kehadiran_id_dosen", table_name="kehadiran")
    op.drop_table("kehadiran")