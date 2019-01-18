def main():
    sideLength = int(input())
    while sideLength > 0:
        rowSums = []
        colSums = []
        matrix = []
        rowToChange = -1
        colToChange = -1
        for i in range(sideLength):
            row = input().split(" ")
            rowSum = 0
            #colSum = 0
            for j in row:
                rowSum += int(j)
            rowSums.append(rowSum)
            matrix.append(row)
        for col in range(sideLength):
            colSum = 0
            for row in range(sideLength):
                colSum += int(matrix[row][col])
            colSums.append(colSum)
        #print(rowSums)
        #print(colSums)
        numOddCol = 0
        numOddRow = 0
        for i in range(sideLength):
            if rowSums[i] % 2 != 0:
                rowToChange = i
                numOddRow += 1
            if colSums[i] % 2 != 0:
                colToChange = i
                numOddCol += 1
        if numOddCol == 0 and numOddRow == 0:
            print("OK")
        elif numOddCol == 1 and numOddRow == 1:
            print("Change bit (" + str(rowToChange + 1) + "," + str(colToChange + 1) + ")")
        else:
            print("Corrupt")

        #print(matrix)

        sideLength = int(input())


main()