def main():
    row = 4
    col = 1
    for i in range(1, 8):
        newRow = row + i
        newCol = col + i
        if newRow < 8 and newCol < 8:
            print(str(newRow) + " " + str(newCol))


main()
