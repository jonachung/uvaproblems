def main():
    line = input()
    while line != "0 0":
        dimensions = line.split()
        row = int(dimensions[0])
        col = int(dimensions[1])
        #rint(row)
        #print(col)

        if row == 1 or col == 1:
            numKnights = row * col
        elif row == 2 and col == 2:
            numKnights = row * col
        elif row == 2 or col == 2:
            if row == 2:
                if col % 4 == 0:
                    numKnights = int(col / 4) * 4
                else:
                    if col % 4 == 1:
                        numKnights = (int(col / 4) * 4) + 2
                    else:
                        numKnights = (int(col / 4) + 1) * 4
            elif col == 2:
                if row % 4 == 0:
                    numKnights = int(row / 4) * 4
                else:
                    if row % 4 == 1:
                        numKnights = (int(row / 4) * 4) + 2
                    else:
                        numKnights = (int(row / 4) + 1) * 4

        else:
            if (row * col) % 2 != 0:
                numKnights = int(((row * col) / 2)) + 1
            else:
                numKnights = int(((row * col) / 2))

        print(str(numKnights) + " knights may be placed on a " + str(row) + " row " + str(col) + " column board.")

        line = input()


main()
