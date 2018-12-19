def rotate90degrees(square):
    newSquare = []
    for col in range(len(square)):
        newRow = []
        for row in range(len(square) - 1, -1, -1):
            newRow.append(square[row][col])
        newSquare.append(newRow)

    return newSquare

def findSquares(bigSquare, smallSquare):
    ans = 0
    for i in range(len(smallSquare)):
        for j in range(len(bigSquare)):
            if i+len(smallSquare) <= len(bigSquare) and j+len(smallSquare) <= len(bigSquare):
                count = 0;
                for k in range(len(smallSquare)):
                    for l in range(len(smallSquare)):
                        if bigSquare[i+k][j+l] == smallSquare[k][l]:
                            count += 1
                if count == len(smallSquare) * len(smallSquare):
                    ans += 1
    return ans


def main():
    rowsOfSquares = input()
    while rowsOfSquares != "0 0":
        rows = rowsOfSquares.split()
        bigRow = int(rows[0])
        smallRow = int(rows[1])
        bigSquare = []
        smallSquare = []
        for row in range(bigRow):
            oneBigRow = list(input())
            bigSquare.append(oneBigRow)
        for row in range(smallRow):
            oneSmallRow = list(input())
            smallSquare.append(oneSmallRow)
        numSquare0 = findSquares(bigSquare, smallSquare)
        square90 = rotate90degrees(smallSquare)
        numSquare90 = findSquares(bigSquare, square90)
        square180 = rotate90degrees(square90)
        numSquare180 = findSquares(bigSquare, square180)
        square270 = rotate90degrees(square180)
        numSquare270 = findSquares(bigSquare, square270)
        print(str(numSquare0) + " " + str(numSquare90) + " " + str(numSquare180) + " " + str(numSquare270))

        rowsOfSquares = input()


main()