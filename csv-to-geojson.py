import csv
import json


def csv_to_geojson(csv_filename, geojson_filename):
    features = []

    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            try:
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                properties = {
                    "id": row['id'],
                    "obiekt_nadawczy": row['obiekt_nadawczy'],
                    "description": row['description'] if row['description'] != 'NULL' else None
                }
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    },
                    "properties": properties
                }
                features.append(feature)
            except ValueError:
                print(f"Błąd konwersji współrzędnych dla ID {row['id']}")

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_filename, 'w', encoding='utf-8') as geojsonfile:
        json.dump(geojson_data, geojsonfile, ensure_ascii=False, indent=4)

    print(f"Plik {geojson_filename} został wygenerowany.")

# Przykładowe użycie:
csv_to_geojson('dane.csv', 'dane.geojson')
