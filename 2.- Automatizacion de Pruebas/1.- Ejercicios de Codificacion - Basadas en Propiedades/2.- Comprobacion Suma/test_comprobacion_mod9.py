from hypothesis import given
from hypothesis.strategies import integers, lists

from comprobacion_suma.comprobacion_mod9 import obtiene_modulo9

numeros = lists(integers(min_value=1000),min_size=2)


@given(k=numeros)
def test_comprobacion(k):
    assert (sum(k))%9 == obtiene_modulo9(k)



@given(l=numeros)
def test_falsos_positivos(l):
    resultado_suma = str((sum(l)))
    resultado_reordenado = ''.join(sorted(resultado_suma))
    assert int(resultado_reordenado)%9 != obtiene_modulo9(l)