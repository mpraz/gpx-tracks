# gpx-tracks

This repository is a collection of GPS Exchange Format (GPX) files, which are used to store and share GPS data.

- Waypoints
- Tracks
- Routes

## Folder structure:

```
GPX Tracks
│
├── Mazury 2023
│   ├── Single Tracks
│   │   ├── Track1.gpx
│   │   ├── Track2.gpx
│   │   └── ...
│   ├── Joined Tracks
│   │   ├── Joined_Mazury_2023.gpx
│   │   └── ...
│   └── Archive
│       ├── Archived_Track1.gpx
│       ├── Archived_Track2.gpx
│       └── ...
│
└── Majorka 2023
    ├── Single Tracks
    │   ├── Track1.gpx
    │   ├── Track2.gpx
    │   └── ...
    ├── Joined Tracks
    │   ├── Joined_Majorka_2023.gpx
    │   └── ...
    └── Archive
        ├── Archived_Track1.gpx
        ├── Archived_Track2.gpx
        └── ...
```

## Explanation of the structure:

GPX Tracks: This is the main folder that contains all your organized GPX data.
Mazury 2023 and Majorka 2023: These are the project-specific subfolders where you store tracks related to each project.
Single Tracks: Inside each project folder, you have a subfolder where you store individual GPX tracks for that project. These are the tracks that haven't been joined or archived.
Joined Tracks: Within each project folder, there's a subfolder where you can save the joined GPX tracks for that project. This could be a combination of all the single tracks for that project.
Archive: This subfolder within each project folder is for storing archived or older GPX tracks that you might not need to access frequently but want to keep for reference.

## File Naming Convention

When saving your GPX files, use a consistent naming convention that includes relevant information. For example:

Flight:

```
Flight_SourceCity_to_DestinationCity.gpx
Car Track: Car_SourceCity_to_DestinationCity.gpx
Bike Track: Bike_SourceCity_to_DestinationCity.gpx
```

Multiple GPX files with same source and destination:

```
Car_SourceCity_to_DestinationCity_1.gpx
Car_SourceCity_to_DestinationCity_2.gpx
Car_SourceCity_to_DestinationCity_2023-08-08.gpx
Car_SourceCity_to_DestinationCity_2023-08-09.gpx
```

In this example, the numerical identifier (1, 2) or the date (2023-08-08, 2023-08-09)

Walking tracks:

```
Walk_SourceCity_to_DestinationCity.gpx
Walk_SourceCity_to_DestinationCity_2023-08-08.gpx
Walk_SourceCity_to_DestinationCity_Morning.gpx
Walk_SourceCity_to_DestinationCity_Evening.gpx
```

In this convention:

Replace SourceCity and DestinationCity with the actual names of the cities you walked between.
You can include a date in YYYY-MM-DD format to indicate when the walk was recorded.
Optionally, you can add a descriptor like Morning or Evening to indicate the time of day when the walk took place.

When you're walking within a single city and you want to name your GPX files to reflect different walks or routes, you can use a simple yet descriptive naming convention. Here's a suggestion:

```
City_Walk1.gpx
City_Walk2.gpx
City_Morning_Walk.gpx
City_Park_Route.gpx
```

In this naming convention:

Replace City with the name of the city where you're walking.
Use a sequential number (1, 2, etc.) to distinguish different walks or routes within the same city.
You can also include descriptors like Morning, Evening, Park, River, or any other relevant identifiers to give an idea of the location or characteristics of the walk.
The idea is to make the file names informative and easily distinguishable, so you can quickly identify the walking routes within the same city.

## Tools

Gimme Geodata to darmowe i niezwykle proste w użyciu narzędzie do szybkiego pobierania map granic z danych OpenStreetMap.

```
https://hanshack.com/geotools/gimmegeodata/
```

```
https://geojson.io/
```

Wyciaganie danych z OSM

```
https://overpass-turbo.eu/
```

Przykłady kwerend dla OverPassTurbo:
Rzeki
["waterway"="stream"]
["waterway"="river"]
Metro:
route=subway

## Sample URL for dynamic tracks

### Trasa Wybrzeze Autem

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/14e9ead714be14fcd25ccff4481105834d58d88a/Baltyk%202023/Single%20Tracks/wybrzeze.geojson
```

### Trasa Wybrzeze Szparag

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/adabe358da0884659f4be2213b6693cdfff35434/Baltyk%202023/Joined%20Tracks/Bike_Swinoujscie_to_Krynica_Szparag.geojson
```

#### R10 filmik

`youtube.com/watch?v=ukh9RFY0jPU`

### Trasa Rolnicy

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/misc/Car_Swarzedz_to_Wroclaw_Rolnicy.geojson
```

### Tyrol

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/4ed03b0b2d4a8613cecdb55c858e35153cf57f48/Tyrol%202022/Single%20Tracks/Car_Garda_Lake.geojson
```

### Rower do Stobnicy

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Single%20Tracks/Bike_Stobnica.geojson
```

### Katania do Katowic 2024

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Sycylia%202024/Single%20Tracks/Flight_Catania_to_Katowice.geojson
```

### Katowice do Katania 2024

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Sycylia%202024/Single%20Tracks/Flight_Katowice_to_Catania.geojson
```

### Katowice - dojazd do lotniska

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Sycylia%202024/Single%20Tracks/Bus_Katowice_to_KatowiceAiport.geojson
```

### Gołuchów - Szczytniki

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/waiting_room_geojson/Car_Goluchow_to_Szczytniki.geojson
```

### Rowerek - Poznań - Malta - jezioro

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Single%20Tracks/Bike_Malta_traditional.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Single%20Tracks/Bike_Malta_Cytadela.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Single%20Tracks/Bike_Swarzedz_Malta.geojson
```

### Poznań do Konin

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Single%20Tracks/Car_Poznan_to_Konin.geojson
```

### Krynica Morska

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Krynica%20Morska%202024/Single%20tracks/Car_Swarzedz_to_Malbork.geojson
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Krynica%20Morska%202024/Single%20tracks/Car_Malbork_to_Krynica.geojson
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Krynica%20Morska%202024/Single%20tracks/Car_Krynica_to_Piaski.geojson
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/Krynica%20Morska%202024/Single%20tracks/Walk_Krynica_Morska_to_Granica.geojson
```

### Poznań - dzielnice

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Swarzedz/poznan_dzielnice.geojson
```

### Swarzedz - Bogucin

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Single%20Tracks/Car_Swarzedz_Bogucin.geojson
```

Rzeki

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/misc/rivers_24_v5.geojson
```

### Drezno

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Drezno%202025/Car_Drezno_to_Swarzedz.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Drezno%202025/Car_Swarzedz_to_Drezno.geojson
```
