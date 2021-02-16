from hypothesis import given
from hypothesis.strategies import integers

from asigna_turno.evalua_edad import *

medio_tiempo=integers(min_value=16, max_value=17)
turno_completo = integers(min_value=18, max_value=64)
invalidos = integers().filter(lambda x: x > 65)
invalidos_menores = integers().filter(lambda x: 16 > x)



@given(k=medio_tiempo)
def test_media_jornada(k):
    assert (asigna_turno(k)) == 1

@given(l=turno_completo)
def test_turno_completo(l):
    assert (asigna_turno(l)) == 2

@given(m=invalidos)
def test_invalidos_jubilados(m):
    assert (asigna_turno(m)) == 0

@given(n=invalidos_menores)
def test_invalidos_menores(n):
    assert (asigna_turno(n)) == 0