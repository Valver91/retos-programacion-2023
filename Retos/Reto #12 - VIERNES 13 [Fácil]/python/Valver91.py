"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""
import calendar

def verificar_viernes_13(mes, año):
    # Obtener el calendario del mes y año especificados
    calendario = calendar.monthcalendar(año, mes)
    
    # Recorrer cada semana del calendario
    for semana in calendario:
        # Verificar si hay un viernes en la semana
        if semana[calendar.FRIDAY] != 0:
            # Verificar si ese día es el 13
            if semana[calendar.FRIDAY] == 13:
                return True
    
    return False

# Solicitar el mes y año al usuario
mes = int(input("Ingrese en el número del mes: "))
año = int(input("¿De que año?: "))

# Verificar si hay un viernes 13 en el mes y año especificados
if verificar_viernes_13(mes, año):
    print("¡Hay un viernes 13 en ese mes y año!")
else:
    print("No hay un viernes 13 en ese mes y año.")