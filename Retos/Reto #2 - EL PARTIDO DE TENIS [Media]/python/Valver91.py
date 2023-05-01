"""
  Escribe un programa que muestre cómo transcurre un juego de tenis 
  y quién lo ha ganado.
  El programa recibirá una secuencia formada por "P1" (Player 1) o 
  "P2" (Player 2), según quien
  gane cada punto del juego.
  
  - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, 
  "Deuce" (empate), ventaja.
  - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], 
  el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el 
 sistema de puntos.   
"""

import os

player1 = 1
player2 = 2

puntuaciones = {0: "Love", 1: "15", 2: "30", 3: "40"}

secuencia = []

def main():

  puntuaciones = {0: "Love", 1: "15", 2: "30", 3: "40"}

  contador_p1 = 0
  contador_p2 = 0

  os.system('clear')

  print("\n                Partido de Tennis    ")
  print('~' * 50)
  print("            | Jugador 1 | Jugador 2 |")
  print("            |-----------|-----------|")
  print(f"            |    {puntuaciones[contador_p1]}   |    {puntuaciones[contador_p2]}   |")

  resultados = []  # lista para almacenar los resultados

  while contador_p1 < 4 and contador_p2 < 4:

    punto = int(input("\n\nSeleccione nº del Jugador para añadir punto (1 o 2): "))
    if punto != 1 and punto != 2:
      print("Por favor elija o Jugador 1 o 2. Gracias.")
    else:
      if punto == 1:
        contador_p1 += 1
      else:
        contador_p2 += 1

    # agrega el resultado actual a la lista de resultados y lo imprime
    if contador_p1 < 4 and contador_p2 < 4:
      resultados.append(f"            |{puntuaciones[contador_p1]}    |{puntuaciones[contador_p2]}    |")
    elif contador_p1 > 4:
      print("Jugador 1 ha ganado")
      break
    elif contador_p2 > 4:
      print("Jugador 2 ha ganado")
      break

    for resultado in resultados:
      print(resultado)
  
  os.system('cls')

  print("\n                Partido de Tennis    ")
  print('~' * 50)
  print("            | Jugador 1 | Jugador 2 |")
  print("            |-----------|-----------|")

  # imprime los resultados almacenados en la lista
  for resultado in resultados:
    print(resultado)

  if contador_p1 >= 4:
    print("¡Jugador 1 gana!")
  else:
    print("¡Jugador 2 gana!")
       


if __name__ == '__main__':
  main()