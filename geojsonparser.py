#!/usr/bin/env python2

#
# This script grabs the input (geojson) file and populates output file
# with SQLite database Coords [Lat_A, Long_A, Lat_B, Long_B, Timestamp]
# by Tworu
#

import json
import sqlite3 as lite
import sys

verbosity = False


def convert(geojson_in, db_out):
    counter = 0
    con = lite.connect(db_out)
    cur = con.cursor()
    cur.executescript("""
            DROP TABLE IF EXISTS Coords;
            CREATE TABLE Coords(Id INTEGER PRIMARY KEY, Lat_A REAL, Long_A REAL, Lat_B REAL, Long_B REAL, Timestamp DATETIME);
            """)

    with open(geojson_in) as f:
        data = json.load(f)

    for feature in data['features']:
        long_a = float(feature['geometry']['coordinates'][0][0])
        lat_a = float(feature['geometry']['coordinates'][0][1])
        long_b = float(feature['geometry']['coordinates'][1][0])
        lat_b = float(feature['geometry']['coordinates'][1][1])
        timestamp = feature['properties']['datetime'].split('T')[0] + ' ' + feature['properties']['datetime'].split('T')[1] + ':00'
        cur.executescript("INSERT INTO Coords(Lat_A, Long_A, Lat_B, Long_B, Timestamp) VALUES (%f,%f,%f,%f,'%s');" % (lat_a, long_a, lat_b, long_b, timestamp))
        if verbosity:
            print timestamp
            print lat_a, long_a, lat_b, long_b
            print "\n"
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
        counter += 1

    print "\n"
    print "Input file: " + geojson_in
    print "Output file: " + db_out
    print "Records written: " + str(counter)
    if con:
        con.close()
    return

if __name__ == "__main__":
    geojson_in = sys.argv[1]
    db_out = sys.argv[2]
    convert(geojson_in, db_out)
