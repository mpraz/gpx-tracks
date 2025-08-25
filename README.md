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

### Sopot

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Sopot_2025/Car_Swarzedz_to_Gdynia.geojson
```

### Praga

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Praga_2025/Car_Wroclaw_to_Praga.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Praga_2025/Car_Praga_to_SzklarskaPoreba.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Praga_2025/Car_SzklarskaPoreba_to_Wroclaw.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Praga_2025/Car_SzklarskaPoreba.geojson
```

### lodz

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

### bieszczady

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/Lodz_2025/Car_Lodz_to_Wroclaw.geojson
```

### Siatka polski

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/siatka_polski.geojson
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/refs/heads/main/siatka_polski_best.geojson
```

## Mapy bazowe

EPSG:3857:5
EPSG:2180:1

W MapLibre GL nie da się mieszać różnych układów współrzędnych (CRS) na jednej mapie — cała mapa musi działać w jednym CRS, najczęściej EPSG:3857. Wszystkie warstwy (vectorowe, rasterowe, WMS itd.) muszą być wtedy zgodne z tym samym układem.

Geoportalowe WMTS-y nie zawsze wspierają EPSG:3857

<TileMatrixSet>
<ows:Identifier>EPSG:2180</ows:Identifier>
Czyli ten serwis działa wyłącznie w układzie EPSG:2180. Nie da się wymusić EPSG:3857 — ten serwis nie udostępnia tej mapy w Web Mercatorze.

MapLibre (bez dodatkowych wtyczek) nie obsłuży WMTS w EPSG:2180, ponieważ:

domyślnie działa tylko w EPSG:3857,

nie ma natywnej obsługi WMTS (trzeba użyć raster layer z raster-dem albo raster źródłem),

i nawet jak użyjesz pluginu maplibre-gl-proj, to musisz mieć styl przygotowany pod EPSG:2180 (własny TileMatrixSet itd.).

https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WMTS/ShadedRelief?service=WMTS&request=getCapabilities --> EPSG:2180
https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WMTS/HypsometryAndShadedRelief?service=WMTS&request=getCapabilities --> EPSG:2180
https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WMTS/Hypsometry?service=WMTS&request=getCapabilities --> EPSG:2180

https://www.labgis.pl/hipso/#9/52.4393/17.9269
https://www.labgis.pl/hipso/arkusz_174.jpg
https://polska.e-mapa.net/

https://sdi.gdos.gov.pl/wms?service=WMS&Request=GetCapabilities
GDOS:ObszaryChronionegoKrajobrazu
GDOS:ObszarySpecjalnejOchrony
GDOS:ParkiKrajobrazowe
GDOS:ParkiNarodowe
GDOS:PomnikiPrzyrody
GDOS:Rezerwaty
GDOS:SpecjalneObszaryOchrony
GDOS:StanowiskaDokumentacyjne
GDOS:UzytkiEkologiczne
GDOS:ZespolyPrzyrodniczoKrajobrazowe

https://bitbucket.org/okulewicz/leaflet/wiki/URLs

Zalety Web Mercator

Web Mercator jest stosowany przez większość serwisów mapowych dostępnych on-line (Google Maps, OpenStreetMap). Jest to standard.
Nowoczesne narzędzia i biblioteki programistyczne do budowy map on-line są zoptymalizowane pod ten układ i wtedy mapa działa najszybciej
Jest to układ odpowiedni dla całego świata
Wady Web Mercator

Jest to układ odpowiedni dla całego świata przez co jego dokładność nie jest geodezyjna. Oznacza to, że niedokładności przy pomiarach są znaczące
Nie wszystkie krajowe usługi danych przestrzennych (np. WMS z Geoportal.gov.pl) są publikowane w tym układzie, przez co konieczna jest reprojekcja co zajmuje czas i może się odbić na jakości danych WMS
Nie jest to optymalny układ do wykorzystania na wydrukach map, a to z kilku powodów.
Dystorsja: EPSG:3857 to układ odniesienia Mercatora (Web Mercator), który znacząco zniekształca obszary, szczególnie na dużych szerokościach geograficznych (na północy i południu). Na mapie w układzie Mercatora, obszary bliskie biegunom wydają się znacznie większe niż są w rzeczywistości, co może prowadzić do błędnych interpretacji danych.
Skala: Z powodu tego zniekształcenia, skala na mapie EPSG:3857 nie jest stała, co może być problematyczne w przypadku wydruków map. Dla mapy internetowej, gdzie użytkownik może przybliżać i oddalać, skala jest mniej istotna, ale na wydruku mapy, skala powinna być stała.
Jednostki: EPSG:3857 używa metrów jako jednostki, ale ze względu na zniekształcenia, te metry nie są „rzeczywistymi” metrami na powierzchni Ziemi, zwłaszcza w pobliżu biegunów.
Jakie są alternatywy?

Jeżeli dane wyświetlane w Systemie mają dotyczyć Polski, to możliwe jest zainstalowanie aplikacji w układzie PUWG 1992 (EPSG:2180), ale dla optymalizacji wyświetlania danych w przeglądarce internetowej, mapa będzie wyświetlana w Web Mercator (EPSG:3857).

https://mapa.wirtualneszlaki.pl/polska-mapa-fizyczna#google_vignette

### hispometria

https://tiles.wirtualneszlaki.pl/DTM-Poland-20m-qgis-z13/8/144/85.png

"tiles": [tiles.wirtualneszlaki.pl/DTM-Poland-20m-qgis-z13/bw-mapnik/{z}/{x}/{y}.png"],

https://gcore.pl/mapy-podkladowe/

https://geoforum.pl/note.php?id=59
https://isok.gov.pl/inspire.html

https://pages.mini.pw.edu.pl/~okulewiczm/leaflet/

### https://bitbucket.org/okulewicz/leaflet/src/master/

inne

https://pages.mini.pw.edu.pl/~okulewiczm/leaflet/04-warstwy-dynamiczne-leaflet/index.html
https://pages.mini.pw.edu.pl/~okulewiczm/leaflet/04-warstwy-dynamiczne-leaflet/map.js
https://pages.mini.pw.edu.pl/~okulewiczm/leaflet/04-warstwy-dynamiczne-leaflet/customLayers.js

### geoportal hypso

"https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WMTS/ShadedRelief?service=WMTS&request=GetTile&version=1.0.0&layer=ISOK_Cien&style=default&format=image/jpeg&TileMatrixSet=EPSG:2180&TileMatrix=EPSG:2180:{z}&TileRow={y}&TileCol={x}"

### Mapproxy

"mapproxy-util serve-develop -b 192.168.2.179:30279 mapproxy.yaml"



https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/GRID1/WMS/ShadedRelief?request=getCapabilities&service=WMS