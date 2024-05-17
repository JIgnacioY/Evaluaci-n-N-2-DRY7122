import requests

def get_route_info(api_key, origin, destination):
    url = f"https://graphhopper.com/api/1/route"
    params = {
        'point': [origin, destination],
        'vehicle': 'car',
        'locale': 'es',
        'instructions': 'true',
        'calc_points': 'true',
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def main():
    api_key = '2e3e1319-c8ed-45b8-b5b9-1b8a1bde6c19'
    while True:
        origin = input("Ciudad de Origen (o 'q' para salir): ")
        if origin.lower() == 'q':
            break
        destination = input("Ciudad de Destino: ")

        origin_coords = {
            'Santiago': '-33.4489,-70.6693',
            'Ovalle': '-30.6015,-71.2000'
        }
        
        if origin not in origin_coords or destination not in origin_coords:
            print("Ciudades no reconocidas. Usa 'Santiago' o 'Ovalle'.")
            continue

        origin_coord = origin_coords[origin]
        destination_coord = origin_coords[destination]

        route_info = get_route_info(api_key, origin_coord, destination_coord)

        try:
            distance = route_info['paths'][0]['distance'] / 1000  
            time = route_info['paths'][0]['time'] / 1000  
            fuel_consumption = distance * 0.1  

            hours = int(time // 3600)
            minutes = int((time % 3600) // 60)
            seconds = int(time % 60)

            print(f"\nNarrativa del viaje de {origin} a {destination}:")
            print(f"Distancia: {distance:.2f} km")
            print(f"Duración: {hours} horas, {minutes} minutos, {seconds} segundos")
            print(f"Combustible requerido: {fuel_consumption:.2f} litros\n")

        except (IndexError, KeyError):
            print("Error al obtener la información de la ruta. Verifique las ciudades e intente nuevamente.")

if __name__ == "__main__":
    main()