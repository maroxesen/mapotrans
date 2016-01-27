# hackuj_slaski_transport
usage:
```
copy trips.geojson
python2 change_file.py FILENAME.geojson PRECISION
where PRECISION is a integer from 10 to 1
```

geojson parser:
```
python2 geojsonparser.py <input.geojson> <output.sqlite>
DB -> Coords [Lat_A, Long_A, Lat_B, Long_B, Timestamp]
```
