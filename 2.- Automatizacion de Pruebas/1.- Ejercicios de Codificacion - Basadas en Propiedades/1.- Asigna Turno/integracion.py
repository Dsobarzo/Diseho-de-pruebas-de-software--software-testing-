from asigna_turno.evalua_edad import asigna_turno
from obtiene_edad import calculate_age


def turno_por_fecha_nacimiento(fecha):
    edad = calculate_age(fecha)
    turno=asigna_turno(edad)
    return turno

