# test
# test2
import csv
from houseClass import houses

# Initiate ID and house list.
ID = 0
house = []

# Open the file containing houses.
with open("Huizen&Batterijen/wijk1_huizen.csv") as f:
    # Read the file and separate values in list.
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    # Skip the header of the file.
    next(f)
    # Create instances of houses in house list.
    for row in reader:
        house.append(houses(ID, row[0], row[1], row[2]))
        ID += 1

# TODO: remove this statement
for i in range(150):
    print(house[i].ID)
