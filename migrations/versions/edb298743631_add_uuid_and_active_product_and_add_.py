"""add uuid and active product and add franchisee table.

Revision ID: edb298743631
Revises: dbd62ca8b5cd
Create Date: 2020-11-06 08:46:13.426300
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'edb298743631'
down_revision = 'dbd62ca8b5cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'product',
        sa.Column('active', sa.Boolean(), server_default='0', nullable=True),
    )
    op.add_column(
        'user',
        sa.Column('franchise_id', sa.Integer(), nullable=True),
    )
    op.add_column('user', sa.Column('uuid', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'uuid')
    op.drop_column('user', 'franchise_id')
    op.drop_column('product', 'active')
    # ### end Alembic commands ###
