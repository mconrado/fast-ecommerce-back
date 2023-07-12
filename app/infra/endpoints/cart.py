from typing import Any
from app.entities.product import ProductCart
from app.infra.bootstrap import Command, bootstrap
from endpoints.deps import get_db
from payment.schema import InstallmentSchema, PaymentResponse
from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy.orm import Session

from domains import domain_order
from endpoints import deps
from payment.service import Checkout
from schemas.order_schema import CheckoutReceive
from app.cart import services

cart = APIRouter(
    prefix='/cart',
    tags=['cart'],
)


async def get_bootstrap() -> Command:
    """Get bootstrap."""
    return await bootstrap()


@cart.post('/product', status_code=201)
async def add_product_to_cart(  # noqa: ANN201
    *,
    uuid: str | None = None,
    product: ProductCart,
    bootstrap: Command = Depends(get_bootstrap),  # noqa: B008
):
    """Add product to cart."""
    # TODO: Implementar o retorno 404 caso produto não exista ou o estoque tenha acabado
    return await services.add_product_to_cart(
        cart_uuid=uuid,
        product=product,
        bootstrap=bootstrap,
    )


@cart.get('/upsell/{id}', status_code=200)
async def get_upsell_products(id):   # noqa: A002, ANN201, ANN001
    """Get upsell products."""
    try:
        # TODO: Implementar o retorno dos produtos upsell
        _ = id
        return True   # noqa: TRY300
    except Exception as e:
        logger.error('Erro ao retornar upsell {e}')
        raise e   # noqa: TRY201


@cart.post('/checkout', status_code=201)
def checkout(
    *,
    db: Session = Depends(deps.get_db),  # noqa: B008
    data: CheckoutReceive,
) -> PaymentResponse:
    """Checkout."""
    checkout_data = data.model_dump().get('transaction')
    affiliate = data.model_dump().get('affiliate')
    cupom = data.model_dump().get('cupom')
    logger.info(checkout_data)
    logger.info(affiliate)
    return Checkout(
        db=db,
        checkout_data=checkout_data,
        affiliate=affiliate,
        cupom=cupom,
    ).process_checkout()


@cart.post('/cart/installments', status_code=200)
async def get_installments(
    *,
    db: Session = Depends(get_db),  # noqa: B008
    cart: InstallmentSchema,
) -> list[Any]:
    """Get installments."""
    try:
        return domain_order.get_installments(db, cart=cart)
    except Exception as e:
        logger.error(f'Erro ao coletar o parcelamento - {e}')
        raise e   # noqa: TRY201