"""add more descriptive column to KyleItem

Revision ID: ec00b5636e94
Revises: 0d6d7b150f41
Create Date: 2023-03-06 16:24:41.204008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec00b5636e94'
down_revision = '0d6d7b150f41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kyle_items', sa.Column('height', sa.Float(), nullable=True))
    op.add_column('kyle_items', sa.Column('superpower', sa.String(), nullable=True))
    op.add_column('kyle_items', sa.Column('weight', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kyle_items', 'weight')
    op.drop_column('kyle_items', 'superpower')
    op.drop_column('kyle_items', 'height')
    # ### end Alembic commands ###
