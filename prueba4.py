import requests

# Función para obtener un Pokémon por nombre
def obtener_pokemon_por_nombre(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        # Extraemos algunos detalles del Pokémon
        nombre = data['name']
        id_pokemon = data['id']
        tipos = [tipo['type']['name'] for tipo in data['types']]
        habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
        
        # Mostramos la información del Pokémon
        return {
            'nombre': nombre,
            'id': id_pokemon,
            'tipos': tipos,
            'habilidades': habilidades
        }
    else:
        print(f"Error: {respuesta.status_code} - No se encontró el Pokémon.")
        return None

# Ejemplo de uso: Buscar el Pokémon por nombre
nombre_pokemon = 'pikachu'  # Cambia el nombre por el que deseas buscar
pokemon = obtener_pokemon_por_nombre(nombre_pokemon)

if pokemon:
    print(f"Información sobre {pokemon['nombre'].capitalize()}:")
    print(f"ID: {pokemon['id']}")
    print(f"Tipos: {', '.join(pokemon['tipos'])}")
    print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
else:
    print(f"No se encontró información para el Pokémon '{nombre_pokemon}'.")