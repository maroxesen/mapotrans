import csv

with open('rozklady2.csv', 'rU') as f:
    reader = csv.reader(f,delimiter=',')
    reader = list(reader)
    points = [[float(line[2]),float(line[3]),int(line[1])] for line in reader]




stops =[]
for item in points:
    point = "POINT ("+str(item[1])+" "+str(item[0])+")"
    stops.append([item[2],point])

with open('przystanki2015.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(stops)