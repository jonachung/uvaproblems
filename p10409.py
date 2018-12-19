def main():
    number = int(input())
    #print(number)
    while number != 0:
        north = 2
        top = 1
        south = 5
        west = 3
        east = 4
        bottom = 6

        for i in range(0, number):
            string = input()
            #print(string)
            temp = top
            if string == "north":
                top = south
                south = bottom
                bottom = north
                north = temp
            elif string == "south":
                top = north
                north = bottom
                bottom = south
                south = temp
            elif string == "east":
                top = west
                west = bottom
                bottom = east
                east = temp
            elif string == "west":
                top = east
                east = bottom
                bottom = west
                west = temp
        print(top)
        number = int(input())

main()