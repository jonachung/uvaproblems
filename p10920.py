def createGrid(lenGrid):
    grid = []
    for row in range(lenGrid):
        gridRow = []
        for col in range(lenGrid):
            gridRow.append("0")
        grid.append(gridRow)

    middleRow = int(lenGrid / 2)
    middleCol = int(lenGrid / 2)
    grid[middleRow][middleCol] = "1"

    if int(lenGrid) > 1:
        count = 1
        maxNumber = lenGrid * lenGrid
        goLeft = 1
        goDownOrRightOrUp = 2
        goUpFirst = 1
        row = middleRow
        col = middleCol
        factor = 2
        while count < maxNumber:
            if count == 1:
                count += 1
            for i in range(goUpFirst):
                row -= 1
                grid[row][col] = str(count)
                count += 1
            for i in range(goLeft):
                col -= 1
                grid[row][col] = str(count)
                count += 1
            goLeft += factor
            for i in range(goDownOrRightOrUp):
                row += 1
                grid[row][col] = str(count)
                count += 1
            for i in range(goDownOrRightOrUp):
                col += 1
                grid[row][col] = str(count)
                count += 1
            for i in range(goDownOrRightOrUp):
                row -= 1
                grid[row][col] = str(count)
                count += 1
            goDownOrRightOrUp += factor

    return grid


def findPosition(grid, position):
    line = 0
    column = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == position:
                column = col + 1
                line = len(grid) - row

    print("Line = " + str(line) + ", column = " + str(column) + ".")


def main():
    numbers = input()
    while numbers != "0 0":
        num = numbers.split()
        lenGrid = int(num[0])
        position = num[1]
        grid = createGrid(lenGrid)
        findPosition(grid, position)
        numbers = input()



main()
