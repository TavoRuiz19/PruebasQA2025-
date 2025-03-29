import requests

# Función para obtener un Pokémon por nombre
def obtener_pokemon_por_nombre(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        
        # Información básica
        nombre = data['name']
        id_pokemon = data['id']
        tipos = [tipo['type']['name'] for tipo in data['types']]
        habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
        
        # Estadísticas
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        
        # Movimientos
        movimientos = [movimiento['move']['name'] for movimiento in data['moves']]
        
        # Construir la información completa
        pokemon_info = {
            'nombre': nombre.capitalize(),
            'id': id_pokemon,
            'tipos': tipos,
            'habilidades': habilidades,
            'estadísticas': stats,
            'movimientos': movimientos[:10]  # Limitamos los primeros 10 movimientos por simplicidad
        }
        
        return pokemon_info
    else:
        print(f"Error: {respuesta.status_code} - No se encontró el Pokémon.")
        return None

# Función para mostrar la información completa del Pokémon
def mostrar_informacion_completa(pokemon):
    if pokemon:
        print(f"Información completa sobre {pokemon['nombre']}:")
        print(f"ID: {pokemon['id']}")
        print(f"Tipos: {', '.join(pokemon['tipos'])}")
        print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
        
        print("\nEstadísticas:")
        for stat, value in pokemon['estadísticas'].items():
            print(f"  {stat.capitalize()}: {value}")
        
        print("\nMovimientos (primeros 10):")
        for i, movimiento in enumerate(pokemon['movimientos'], start=1):
            print(f"  {i}. {movimiento}")
    else:
        print("No se encontró información para este Pokémon.")

# Ejemplo de uso: Buscar y mostrar información del Pokémon
nombre_pokemon = 'pikachu'  # Cambia el nombre por el que deseas buscar
pokemon = obtener_pokemon_por_nombre(nombre_pokemon)

mostrar_informacion_completa(pokemon)