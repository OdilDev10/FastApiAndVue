"""Add owner table pets

Revision ID: 1649aa7d1d51
Revises: 04573532376d
Create Date: 2023-12-09 22:53:35.655839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1649aa7d1d51'
down_revision: Union[str, None] = '04573532376d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('pets', sa.Column('owner', sa.Integer, nullable=True))


def downgrade():
    op.drop_column('pets', 'owner')