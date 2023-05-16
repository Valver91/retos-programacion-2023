"""
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""
def get_parameters(url):
    
    # Dividir la URL en dos partes: la URL base y los parámetros
    parameters=url.split('?')
    
    # Separar los parámetros individuales
    parameters=parameters[1].split('&')
    
    # Crear una lista vacía para almacenar los valores de los parámetros
    values=[]
    
    # Recorrer cada parámetro y extraer el valor
    for each in parameters:
        parameter=each.split("=")
        values.append(parameter[1])
    
    # Devolver la lista de valores de los parámetros
    return (values)

print(get_parameters('https://retosdeprogramacion.com?year=2023&challenge=0'))