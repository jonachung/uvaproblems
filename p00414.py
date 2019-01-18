def main():
    numRows = int(input())
    while numRows != 0:
        listOfRows = []
        listOfSpaces = []
        totalvoid = 0
        for i in range(numRows):
            row = input()
            listOfRows.append(row)
        for row in listOfRows:
            spaces = row.count(" ")
            listOfSpaces.append(spaces)
        minSpace = min(listOfSpaces)
        for space in listOfSpaces:
            diff = space - minSpace
            totalvoid += diff

        print(totalvoid)

        numRows = int(input())



main()

