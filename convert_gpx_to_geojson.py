import os
import gpxpy
import geojson
from geojson import Feature, FeatureCollection, LineString


def convert_gpx_to_geojson(gpx_file_path):
    with open(gpx_file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    features = []
    for track in gpx.tracks:
        for segment in track.segments:
            coordinates = []
            for point in segment.points:
                coordinates.append((point.longitude, point.latitude, point.elevation))
            if coordinates:
                features.append(Feature(geometry=LineString(coordinates)))

    return FeatureCollection(features)


def convert_all_gpx_to_geojson(gpx_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(gpx_dir):
        if filename.endswith('.gpx'):
            gpx_file_path = os.path.join(gpx_dir, filename)
            try:
                geojson_data = convert_gpx_to_geojson(gpx_file_path)
                geojson_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.geojson')

                with open(geojson_file_path, 'w') as geojson_file:
                    geojson.dump(geojson_data, geojson_file, indent=2)

                print(f'Converted {filename} to GeoJSON.')
            except Exception as e:
                print(f'Error converting {filename}: {e}')


if __name__ == "__main__":
    gpx_directory = r'C:\Users\dlxpgh2\Desktop\trackExport 2'
    output_directory = r'C:\Users\dlxpgh2\Desktop\trackExport 2\geojson'

    convert_all_gpx_to_geojson(gpx_directory, output_directory)
