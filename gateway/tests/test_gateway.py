import pytest

from gateway.payment_gateway import return_transaction


@pytest.mark.skip()
def test_return_transaction():
    transaction = return_transaction(10919263)
    assert transaction.get('gateway_id') == 10919263
