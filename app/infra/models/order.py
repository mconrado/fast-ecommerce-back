from datetime import datetime
from decimal import Decimal
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, backref, mapped_column, relationship
from sqlalchemy.types import JSON

from app.infra.models.base import Base


class Category(Base):
    __tablename__ = 'category'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    path: Mapped[str]


class Product(Base):
    __tablename__ = 'product'

    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    uri: Mapped[str]
    price: Mapped[Decimal]
    active: Mapped[bool] = mapped_column(default=False)
    direct_sales: Mapped[bool] = mapped_column(default=False)
    description: Mapped[str]
    image_path: Mapped[str | None]
    installments_config: Mapped[int]
    installments_list: Mapped[dict] = mapped_column(JSON, nullable=True)
    discount: Mapped[int | None]
    category_id: Mapped[int] = mapped_column(
        ForeignKey('category.category_id'),
    )
    category: Mapped['Category'] = relationship(
        foreign_keys=[category_id],
        backref='Product',
        cascade='all,delete',
        uselist=False,
    )
    showcase: Mapped[bool] = mapped_column(default=False)
    show_discount: Mapped[bool] = mapped_column(default=False)
    height: Mapped[Decimal | None]
    width: Mapped[Decimal | None]
    weight: Mapped[Decimal | None]
    length: Mapped[Decimal | None]
    diameter: Mapped[Decimal | None]
    sku: Mapped[str]


class Coupons(Base):
    __tablename__ = 'coupons'

    coupon_id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    discount: Mapped[Decimal]
    qty: Mapped[int]
    active: Mapped[bool] = mapped_column(default=True)


class Order(Base):
    __tablename__ = 'order'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    user = relationship(
        'User',
        foreign_keys=[customer_id],
        backref='Order',
        cascade='all,delete',
        uselist=False,
    )
    order_date: Mapped[datetime]
    tracking_number: Mapped[str | None]
    payment_id: Mapped[int | None] = mapped_column(
        ForeignKey('payment.payment_id'),
    )
    order_status: Mapped[str]
    last_updated: Mapped[datetime]
    checked: Mapped[bool] = mapped_column(default=False)


class OrderItems(Base):
    __tablename__ = 'order_items'

    order_items_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'))
    order = relationship(
        'Order',
        backref=backref('order_items', uselist=False),
        cascade='all,delete',
        foreign_keys=[order_id],
    )
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))
    product = relationship(
        'Product',
        backref=backref('product', uselist=False),
        cascade='all,delete',
        foreign_keys=[product_id],
    )
    quantity: Mapped[int]


class OrderStatusSteps(Base):
    __tablename__ = 'order_status_steps'

    order_status_steps_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.order_id'))
    status: Mapped[str]
    last_updated: Mapped[datetime]
    sending: Mapped[bool]
    active: Mapped[bool]


class ImageGallery(Base):
    __tablename__ = 'image_gallery'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    product_id: Mapped[int] = mapped_column(ForeignKey('product.product_id'))
