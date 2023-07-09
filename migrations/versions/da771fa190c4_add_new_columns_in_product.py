"""add new columns in product.

Revision ID: da771fa190c4
Revises: 54e9f30a86d3
Create Date: 2020-11-19 12:00:05.150049
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'da771fa190c4'
down_revision = '54e9f30a86d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'product',
        sa.Column(
            'category_id',
            sa.Integer(),
            server_default='1',
            nullable=True,
        ),
    )
    op.add_column(
        'product',
        sa.Column('discount', sa.Integer(), nullable=True),
    )
    op.add_column(
        'product',
        sa.Column(
            'quantity',
            sa.Integer(),
            server_default='9999',
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'quantity')
    op.drop_column('product', 'discount')
    op.drop_column('product', 'category_id')
    # ### end Alembic commands ###
