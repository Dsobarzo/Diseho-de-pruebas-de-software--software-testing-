from datetime import datetime
from datetime import timedelta

from dateutil.relativedelta import relativedelta
from hypothesis import given
from hypothesis.strategies import dates

from asigna_turno.integracion import turno_por_fecha_nacimiento


def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    return (from_date - relativedelta(years=years)).date()



medio_tiempo=dates(min_date=yearsago(18)+ timedelta(days=1),max_date=yearsago(16))
turno_completo = dates(min_date=yearsago(65)+ timedelta(days=1),max_date=yearsago(18))
invalidos=dates(max_date=yearsago(65))
invalidos_menores = dates(min_date=yearsago(16)+ timedelta(days=1))

@given(k=medio_tiempo)
def test_medio_jornada(k):
    assert (turno_por_fecha_nacimiento(k)) == 1

@given(l=turno_completo)
def test_jornada_completo(l):
    assert (turno_por_fecha_nacimiento(l)) == 2

@given(m=invalidos)
def test_jubilados(m):
    assert (turno_por_fecha_nacimiento(m)) == 0

@given(n=invalidos_menores)
def test_menores(n):
    assert (turno_por_fecha_nacimiento(n)) == 0