"""
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
"""

import requests

# Make a GET request to the Chuck Norris Jokes API
response = requests.get('https://api.chucknorris.io/jokes/random')

# Check if the request was successful
if response.status_code == 200:
    # If the request was successful, extract the joke and print it
    joke = response.json()['value']
    print(joke)
else:
    # If the request was not successful, print an error message
    print('An error occurred while getting the Chuck Norris joke')