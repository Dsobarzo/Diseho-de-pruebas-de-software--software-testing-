def asigna_turno(edad):
    if edad >=16 and edad < 18:
        return 1
    elif edad >= 18 and edad <65:
        return 2
    else:
        return 0


print asigna_turno(14)