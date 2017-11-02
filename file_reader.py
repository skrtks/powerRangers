import csv
import sys
from houseClass import houses

if not len(sys.argv) == 2:
    print("Usage: filename")

ID = 0
house = []
with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        house.append(houses(ID, row[0], row[1], row[2]))
        ID += 1

for i in range(5):
    print(house[i].power)
