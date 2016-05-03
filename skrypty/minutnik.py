import csv

with open('rozklady.csv', 'rU') as f:
    reader = csv.reader(f,delimiter=',')
    reader = list(reader)

nets=[]
for net in reader:
    netrow=[]
    for item in net:
        if item != "":
            colon = item.find(":")
            dot = item.find(".")
            if colon != -1: index = colon
            if dot != -1: index = dot
            hour = int(item[0:index])
            minute = int(item[index+1:index+3])
            time = hour*60+minute
            netrow.append(time)
    print netrow
    nets.append(netrow)

print nets

with open('skm.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(nets)
