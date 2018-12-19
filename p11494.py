def main():
    line = input()
    while line != "0 0 0 0":
        positions = line.split()
        row1 = int(positions[0])
        col1 = int(positions[1])
        row2 = int(positions[2])
        col2 = int(positions[3])
        if row1 == row2 and col1 == col2:
            print("0")
        else:
            rise = abs(col1 - col2)
            run = abs(row1 - row2)

            if rise == run:
                print("1")
            elif row1 != row2 and col1 == col2:
                print("1")
            elif row1 == row2 and col1 != col2:
                print("1")
            else:
                print("2")
        line = input()


main()
