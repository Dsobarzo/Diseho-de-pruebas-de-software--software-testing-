from hypothesis import given, example
from hypothesis.strategies import dates
from obtiene_edad import calculate_age
from datetime import date

fechas=dates()


@given(k=fechas)
def test_reciproco_fecha(k):
    today = date.today()
    assert today.year - calculate_age(k) - ((today.month, today.day) < (k.month, k.day)) == k.year

