
def obtiene_modulo9(lista_numeros):
    array_resultados=[]
    for numero in lista_numeros:
        array_resultados.append(numero%9)
    suma_modulos=sum(array_resultados)
    suma_modulos=suma_modulos%9
    return suma_modulos




