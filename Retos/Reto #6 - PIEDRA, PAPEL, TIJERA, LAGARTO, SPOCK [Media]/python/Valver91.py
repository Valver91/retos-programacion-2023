"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
*/

/*
 * Normas del juego:
    Las tijeras cortan el papel, el papel envuelve la piedra, 
    la piedra aplasta al lagarto, el lagarto envenena a Spock, 
    Spock aplasta las tijeras, las tijeras decapitan al lagarto, 
    el lagarto devora el papel, el papel desaprueba a Spock, 
    Spock desintegra la piedra y, como siempre, la piedra aplasta las tijeras.
*/

/*
 * En mi version, he definido las relglas del juego. Despues mediante un input, 
   le pido al Jugador 1 que introduzca el valor de lo que desea hacer, e importando
   la función random hago que el supuesto jugador 2 (que es la "máquina") lance su 
   jugada y según las reglas imprima el ganador.
   El juego termina al completar 3 rondas.
*/
"""

import random

def jugar_pipatilas():
    reglas = {1: {2: "Player 2", 3: "Player 1", 4: "Player 1", 5: "Player 2"},
              2: {1: "Player 1", 3: "Player 2", 4: "Player 2", 5: "Player 1"},
              3: {1: "Player 2", 2: "Player 1", 4: "Player 2", 5: "Player 1"},
              4: {1: "Player 2", 2: "Player 1", 3: "Player 1", 5: "Player 2"},
              5: {1: "Player 1", 2: "Player 2", 3: "Player 2", 4: "Player 1"}}

    jugadas = {1: "🗿", 2: "📄", 3: "✂️", 4: "🦎", 5: "🖖"}

    puntuacion = {"Player 1": 0, "Player 2": 0}

    while True:
        print("Jugadas:")
        for jugada in jugadas.items():
            print(f"{jugada[0]}: {jugada[1]}")
        jugador_1 = int(input("Jugador 1: seleccione su jugada (1-5): "))
        if jugador_1 not in jugadas:
            print("Jugada no válida. Inténtalo de nuevo.")
            continue
        jugador_2 = random.choice(list(jugadas.keys()))
        print(f"Jugador 2: {jugadas[jugador_2]}")

        if jugador_1 == jugador_2:
            print("Empate.")
        elif reglas[jugador_1][jugador_2] == "Player 1":
            print("Jugador 1 gana esta ronda.")
            puntuacion["Player 1"] += 1
        else:
            print("Jugador 2 gana esta ronda.")
            puntuacion["Player 2"] += 1

        if puntuacion["Player 1"] == 3:
            return "Player 1 gana el juego."
        elif puntuacion["Player 2"] == 3:
            return "Player 2 gana el juego."

        
resultado = jugar_pipatilas()
print(resultado)