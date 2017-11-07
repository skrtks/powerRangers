import csv
from houseClass import houses
from batteryClass import batteries
from matplotlib import pyplot as plt

def main():
    file_reader("Huizen&Batterijen/wijk1_huizen.csv", "Huizen&Batterijen/wijk1_batterijen.csv")


def file_reader(file_houses, file_batteries):

    # Initiate ID and house list.
    ID = 0
    house = []
    battery = []

    # Open the file containing houses.
    with open(file_houses) as h, open(file_batteries) as b:
        # Read the file and separate values in list.
        reader_houses = csv.reader(h, delimiter=',', quoting=csv.QUOTE_NONE)
        reader_batteries = csv.reader(b, delimiter=',', quoting=csv.QUOTE_NONE)
        # Skip the header of the file.
        next(h)
        next(b)

        # Create instances of houses or batteries.
        for row in reader_houses:
            house.append(houses(ID, row[0], row[1], row[2]))
            ID += 1
        for row in reader_batteries:
            battery.append(batteries(ID, row[0], row[1], row[2]))
            ID += 1

        for i in range(5):
            print(house[i].xLocation, battery[i].yLocation)


#def draw_grid():
        # get coordinates
        coordinates_x = []
        coordinates_y = []

        for i in range(150):
            coordinates_x.append(int(house[i].xLocation))
            coordinates_y.append(int(house[i].yLocation))

        x = coordinates_x
        y = coordinates_y

        plt.scatter(x, y)
        plt.show()

if __name__ == "__main__":
    main()
