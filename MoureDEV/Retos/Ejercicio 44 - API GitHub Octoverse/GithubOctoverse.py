# /*
#  * EJERCICIO:
#  * GitHub ha publicado el Octoverse 2024, el informe
#  * anual del estado de la plataforma:
#  * https://octoverse.github.com
#  *
#  * Utilizando el API de GitHub, crea un informe asociado
#  * a un usuario concreto.
#  *
#  * - Se debe poder definir el nombre del usuario
#  *   sobre el que se va a generar el informe.
#  *
#  * - Crea un informe de usuario basándote en las 5 métricas
#  *   que tú quieras, utilizando la informración que te
#  *   proporciona GitHub. Por ejemplo:
#  *   - Lenguaje más utilizado
#  *   - Cantidad de repositorios
#  *   - Seguidores/Seguidos
#  *   - Stars/forks
#  *   - Contribuciones
#  *   (lo que se te ocurra)
#  */

import requests

user = input("Indica el nombre de usuario del que generar el informe: ")
token = "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"
header = {'Authorization': f"Bearer {token}"}
URI = f"https://api.github.com/users/{user}"

respuesta = requests.get(URI, headers=header).json()
repos = requests.get(URI+"/repos", headers=header).json()

public_repos = respuesta["public_repos"]
followers = respuesta["followers"]
following = respuesta["following"]


def stars():
    # stargazers_count
    global stars
    stars = 0
    for rep in repos:
        stars += rep["stargazers_count"]


def forks():
    # forks
    global forks
    forks = 0
    for rep in repos:
        forks += rep["forks"]


stars()
forks()
informe = (f"""

A continuación se muestra el informe del usuario {user}:
    
    Cantidad de repositorios:       {public_repos}
    Seguidores:                     {followers}
    Seguidos:                       {following}
    Estrellas:                      {stars}
    Forks:                          {forks}

    """)

print(informe)
