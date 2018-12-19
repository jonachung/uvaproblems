def main():
    fieldNum = 1
    rowCol = input()
    while rowCol != "0 0":
        if fieldNum != 1:
            print("")
        rowColumn = rowCol.split()
        rowNum = int(rowColumn[0])
        colNum = int(rowColumn[1])
        #print(rowNum)
        #print(colNum)
        mineSweeperArray = []
        for i in range(0, rowNum):
            row = list(input())
            mineSweeperArray.append(row)
        print("Field #" + str(fieldNum) + ":")
        #print(mineSweeperArray)
        answer = []
        for i in range(0, rowNum):
            answerRow = []
            for j in range(0, colNum):
                answerRow.append(0)
            answer.append(answerRow)
        #print(answer)
        for i in range(0, rowNum):
            for j in range(0, colNum):
                #print(i)
                #print(j)
                if mineSweeperArray[i][j] == "*":
                    if i - 1 >= 0 and j - 1 >= 0 and i - 1 < rowNum and j - 1 < colNum and mineSweeperArray[i - 1][j - 1] == ".":
                        answer[i - 1][j - 1] += 1
                        #print("Top left diag")
                        #print(answer)
                    if i >= 0 and j - 1 >= 0 and i < rowNum and j - 1 < colNum and mineSweeperArray[i][j - 1] == ".":
                        #print("left")
                        answer[i][j - 1] += 1
                        #print(answer)
                    if i + 1 >= 0 and j - 1 >= 0 and i + 1 < rowNum and j - 1 < colNum and mineSweeperArray[i + 1][j - 1] == ".":
                        answer[i + 1][j - 1] += 1
                        #print("bottom left diag")
                        #print(answer)
                    if i + 1 >= 0 and j >= 0 and i + 1 < rowNum and j < colNum and mineSweeperArray[i + 1][j] == ".":
                        answer[i + 1][j] += 1
                        #print("bottom")
                        #print(answer)
                    if i - 1 >= 0 and j >= 0 and i - 1 < rowNum and j < colNum and mineSweeperArray[i - 1][j] == ".":
                        answer[i - 1][j] += 1
                        #print("top")
                        #print(answer)
                    if i - 1 >= 0 and j + 1 >= 0 and i - 1 < rowNum and j + 1 < colNum and mineSweeperArray[i - 1][j + 1] == ".":
                        answer[i - 1][j + 1] += 1
                        #print("top right diag")
                        #print(answer)
                    if i >= 0 and j + 1 >= 0 and i < rowNum and j + 1 < colNum and mineSweeperArray[i][j + 1] == ".":
                        answer[i][j + 1] += 1
                        #print("right")
                        #print(answer)
                    if i + 1 >= 0 and j + 1 >= 0 and i + 1 < rowNum and j + 1 < colNum and mineSweeperArray[i + 1][j + 1] == ".":
                        answer[i + 1][j + 1] += 1
                        #print("bottom right diag")
                        #print(answer)
        for i in range(0, rowNum):
             for j in range(0, colNum):
                 if mineSweeperArray[i][j] == "*":
                     print("*", end="")
                 else:
                     print(str(answer[i][j]), end="")
             print("")

        rowCol = input()
        fieldNum = fieldNum + 1

main()