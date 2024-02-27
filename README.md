# gpx-tracks
repository of my exploration

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
Car_SourceCity_to_DestinationCity_1.gpx
Car_SourceCity_to_DestinationCity_2.gpx
Car_SourceCity_to_DestinationCity_2023-08-08.gpx
Car_SourceCity_to_DestinationCity_2023-08-09.gpx
In this example, the numerical identifier (1, 2) or the date (2023-08-08, 2023-08-09)

Walking tracks:
Walk_SourceCity_to_DestinationCity.gpx
Walk_SourceCity_to_DestinationCity_2023-08-08.gpx
Walk_SourceCity_to_DestinationCity_Morning.gpx
Walk_SourceCity_to_DestinationCity_Evening.gpx
In this convention:

Replace SourceCity and DestinationCity with the actual names of the cities you walked between.
You can include a date in YYYY-MM-DD format to indicate when the walk was recorded.
Optionally, you can add a descriptor like Morning or Evening to indicate the time of day when the walk took place.

When you're walking within a single city and you want to name your GPX files to reflect different walks or routes, you can use a simple yet descriptive naming convention. Here's a suggestion:

City_Walk1.gpx
City_Walk2.gpx
City_Morning_Walk.gpx
City_Park_Route.gpx
In this naming convention:

Replace City with the name of the city where you're walking.
Use a sequential number (1, 2, etc.) to distinguish different walks or routes within the same city.
You can also include descriptors like Morning, Evening, Park, River, or any other relevant identifiers to give an idea of the location or characteristics of the walk.
The idea is to make the file names informative and easily distinguishable, so you can quickly identify the walking routes within the same city.



### Sample URL for dynamic tracks
```
-- Trasa Wybrzeze
```

```
https://raw.githubusercontent.com/mpraz/gpx-tracks/14e9ead714be14fcd25ccff4481105834d58d88a/Baltyk%202023/Single%20Tracks/wybrzeze.geojson
```
-- Trasa Wybrzeze Szparag
```
https://raw.githubusercontent.com/mpraz/gpx-tracks/adabe358da0884659f4be2213b6693cdfff35434/Baltyk%202023/Joined%20Tracks/Bike_Swinoujscie_to_Krynica_Szparag.geojson
```

-- Trasa Rolnicy
```
https://raw.githubusercontent.com/mpraz/gpx-tracks/main/misc/Car_Swarzedz_to_Wroclaw_Rolnicy.geojson
```
