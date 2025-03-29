import requests

# Función para obtener Pokémon por tipo
def obtener_pokemon_por_tipo(tipo):
    url = f"https://pokeapi.co/api/v2/type/{tipo}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        # Filtrar los Pokémon
        pokemones = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        return pokemones
    else:
        print(f"Error: {respuesta.status_code}")
        return []

# Ejemplo de uso: Filtrar Pokémon de tipo 'fire'
tipo = 'fire'  # Puedes cambiar 'fire' por el tipo que quieras (por ejemplo, 'water', 'grass', etc.)
pokemones = obtener_pokemon_por_tipo(tipo)

if pokemones:
    print(f"Pokémon de tipo {tipo}:")
    for pokemon in pokemones:
        print(pokemon)
else:
    print(f"No se encontraron Pokémon para el tipo {tipo}.")