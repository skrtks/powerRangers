import csv
from houseClass import houses
from batteryClass import batteries
from matplotlib import pyplot as plt

def main():
    file_reader("Huizen&Batterijen/wijk1_huizen.csv", "house")


def file_reader(file_name, class_name):

    # Initiate ID and house list.
    ID = 0
    house = []
    battery = []

    # Open the file containing houses.
    with open(file_name) as f:
        # Read the file and separate values in list.
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # Skip the header of the file.
        next(f)

        # Create instances of houses or batteries.
        if class_name == "house":
            for row in reader:
                house.append(houses(ID, row[0], row[1], row[2]))
                ID += 1
        elif class_name == "battery":
            for row in reader:
                battery.append(batteries(ID, row[0], row[1], row[2]))
                ID += 1

        #for i in range(150):
            #print(house[0].xLocation, house[0].yLocation)

#def draw_grid():
        # get coordinates
        coordinates_x = []
        coordinates_y = []

        for i in range(150):
            coordinates_x.append(int(house[i].xLocation))
            coordinates_y.append(int(house[i].yLocation))

        # draw scatterplot
        x = coordinates_x
        y = coordinates_y

        plt.scatter(x, y, s=50)
        plt.grid()

        plt.show()

if __name__ == "__main__":
    main()
