"""add new columns in product.

Revision ID: 6f91dc2c2189
Revises: da771fa190c4
Create Date: 2020-11-21 09:58:35.544494
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6f91dc2c2189'
down_revision = 'da771fa190c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'product',
        sa.Column(
            'show_discount',
            sa.Boolean(),
            server_default='0',
            nullable=True,
        ),
    )
    op.add_column(
        'product',
        sa.Column('showcase', sa.Boolean(), server_default='0', nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'showcase')
    op.drop_column('product', 'show_discount')
    # ### end Alembic commands ###
