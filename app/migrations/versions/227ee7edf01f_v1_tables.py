"""v1 tables

Revision ID: 227ee7edf01f
Revises: 
Create Date: 2020-10-27 13:52:03.255023

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "227ee7edf01f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("type_address", sa.String(), nullable=True),
        sa.Column("category", sa.String(), nullable=True),
        sa.Column("country", sa.String(length=58), nullable=True),
        sa.Column("city", sa.String(length=58), nullable=True),
        sa.Column("state", sa.String(length=58), nullable=True),
        sa.Column("neighborhood", sa.String(length=58), nullable=True),
        sa.Column("street", sa.String(), nullable=True),
        sa.Column("street_number", sa.String(), nullable=True),
        sa.Column("address_complement", sa.String(), nullable=True),
        sa.Column("zipcode", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "creditcardfeeconfig",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("min_installment_with_fee", sa.Integer(), nullable=True),
        sa.Column("mx_installments", sa.Integer(), nullable=True),
        sa.Column("fee", sa.Numeric(), nullable=True),
        sa.Column(
            "active_date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "orderstatussteps",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.Column("sending", sa.Boolean(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("uri", sa.String(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column("direct_sales", sa.Boolean(), nullable=True),
        sa.Column("upsell", postgresql.ARRAY(sa.Integer()), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("image_path", sa.String(), nullable=True),
        sa.Column("installments_config", sa.Integer(), nullable=True),
        sa.Column("installments_list", postgresql.ARRAY(sa.JSON()), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "role",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=True),
        sa.Column("role", sa.String(length=64), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "uploadedimage",
        sa.Column("id", sa.String(length=512), nullable=False),
        sa.Column("original", sa.String(length=512), nullable=True),
        sa.Column("small", sa.String(length=512), nullable=True),
        sa.Column("thumb", sa.String(length=512), nullable=True),
        sa.Column("icon", sa.String(length=512), nullable=True),
        sa.Column("uploaded", sa.Boolean(), nullable=True),
        sa.Column("mimetype", sa.String(length=48), nullable=True),
        sa.Column("name", sa.String(length=512), nullable=True),
        sa.Column("size", sa.String(length=24), nullable=True),
        sa.Column("image_bucket", sa.String(length=48), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=512), nullable=True),
        sa.Column("document", sa.String(length=32), nullable=True),
        sa.Column(
            "document_type",
            sa.String(length=32),
            server_default="CPF",
            nullable=True,
        ),
        sa.Column("birth_date", sa.DateTime(), nullable=True),
        sa.Column("gender", sa.String(length=32), nullable=True),
        sa.Column("email", sa.String(length=128), nullable=True),
        sa.Column("phone", sa.String(length=128), nullable=True),
        sa.Column(
            "user_timezone",
            sa.String(length=50),
            server_default="America/Sao_Paulo",
            nullable=True,
        ),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(length=20), nullable=True),
        sa.Column(
            "update_email_on_next_login",
            sa.Boolean(),
            server_default="0",
            nullable=True,
        ),
        sa.Column(
            "update_password_on_next_login",
            sa.Boolean(),
            server_default="0",
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "order",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("customer_id", sa.Integer(), nullable=True),
        sa.Column("order_date", sa.DateTime(), nullable=True),
        sa.Column("tracking_number", sa.Integer(), nullable=True),
        sa.Column("payment_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "payment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("amount", sa.Integer(), nullable=True),
        sa.Column("token", sa.String(length=25), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("authorization", sa.String(), nullable=True),
        sa.Column("payment_method", sa.String(), nullable=True),
        sa.Column("payment_gateway", sa.String(), nullable=True),
        sa.Column("installments", sa.Integer(), nullable=True),
        sa.Column("processed", sa.Boolean(), server_default="0", nullable=False),
        sa.Column("processed_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "transaction",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("amount", sa.Integer(), nullable=True),
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column("qty", sa.Integer(), nullable=True),
        sa.Column("payment_id", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("affiliate", sa.String(), nullable=True),
        sa.Column("affiliate_quota", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "orderitems",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["order.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orderitems")
    op.drop_table("transaction")
    op.drop_table("payment")
    op.drop_table("order")
    op.drop_table("user")
    op.drop_table("uploadedimage")
    op.drop_table("role")
    op.drop_table("product")
    op.drop_table("orderstatussteps")
    op.drop_table("creditcardfeeconfig")
    op.drop_table("address")
    # ### end Alembic commands ###
