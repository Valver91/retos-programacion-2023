"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

from random import *
import secrets
import string

def pass_gen():
    pws_lenght = int(input("Enter the desired length: "))
    while pws_lenght < 8 or pws_lenght > 16:
        print("please, the length has to be a minimum of 8 and a maximum of 16.")
        pws_lenght = int(input("Enter the desired length: "))

    letters = input("Do you want it to contain letters? y/n: ").lower()
    while letters not in ["y", "n"]:
        print("Please write y or n.")
        letters = input("Do you want to include letters? (y/n): ")
    if letters == "y":
        letters = string.ascii_letters
    else:
        letters = ''

    numbers = input("Do you want it to contain numbers? y/n: ").lower()
    while numbers not in ["y", "n"]:
        print("Please write y or n.")
        numbers = input("Do you want to include numbers? (y/n): ")
    if numbers:
        numbers = string.digits
    else:
        numbers = ''

    spec_chars = input("Do you want it to contain special characters? y/n: ").lower()
    while spec_chars not in ["y", "n"]:
        print("Please write y or n.")
        spec_chars = input("Do you want to include special characters? (y/n): ")
    if spec_chars:
        spec_chars = string.punctuation
    else:
        spec_chars = ''
        
    password = letters + numbers + spec_chars

    code = ''
    for i in range(pws_lenght):
        code += ''.join(secrets.choice(password))

    print(code)

pass_gen()