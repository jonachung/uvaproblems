def changeAdjacentSquares():
    pass


def addToNewKingdom():
    pass


def simulateBattle(kingdom, numHeirs, numRows, numCols):
    newKingdom = []
    for i in range(numRows):
        row = []
        for j in range(numCols):
            row.append("-")
        newKingdom.append(row)
    for i in range(numRows):
        for j in range(numCols):
            heir = int(kingdom[i][j])
            isLastHeir = heir == str(numHeirs - 1)  ## if last heir, then attacks first heir
            if i == 0 and j == 0:
                if isLastHeir:
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j + 1] == str(heir + 1):
                        newKingdom[i][j + 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif 0 < i < len(kingdom) - 1 and j == 0:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j + 1] == str(heir + 1):
                        newKingdom[i][j + 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif i == len(kingdom) - 1 and j == 0:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i][j + 1] == str(heir + 1):
                        newKingdom[i][j + 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif i == len(kingdom) - 1 and 0 < j < len(kingdom[i]) - 1:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i][j + 1] == str(heir + 1):
                        newKingdom[i][j + 1] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif i == len(kingdom) - 1 and j == len(kingdom[i]) - 1:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif 0 < i < len(kingdom) - 1 and j == len(kingdom[i]) - 1:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif i == 0 and j == len(kingdom[0]) - 1:
                if isLastHeir:
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    newKingdom[i][j] = str(heir)
            elif i == 0 and 0 < j < len(kingdom[0]) - 1:
                if isLastHeir:
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    if newKingdom[i][j] == "-":
                        newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i][j + 1] == str(heir + 1):
                        print(kingdom[i][j + 1])
                        newKingdom[i][j + 1] = str(heir)
                        print(newKingdom)
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    if newKingdom[i][j] == "-":
                        newKingdom[i][j] = str(heir)
                    print(newKingdom)
            elif 0 < i < len(kingdom) - 1 and 0 < j < len(kingdom[i]) - 1:
                if isLastHeir:
                    if kingdom[i - 1][j] == "0":
                        newKingdom[i - 1][j] = str(numHeirs - 1)
                    if kingdom[i][j + 1] == "0":
                        newKingdom[i][j + 1] = str(numHeirs - 1)
                    if kingdom[i + 1][j] == "0":
                        newKingdom[i + 1][j] = str(numHeirs - 1)
                    if kingdom[i][j - 1] == "0":
                        newKingdom[i][j - 1] = str(numHeirs - 1)
                    #if newKingdom[i][j] == "-":
                    newKingdom[i][j] = str(numHeirs - 1)
                else:
                    if kingdom[i - 1][j] == str(heir + 1):
                        newKingdom[i - 1][j] = str(heir)
                    if kingdom[i][j + 1] == str(heir + 1):
                        newKingdom[i][j + 1] = str(heir)
                    if kingdom[i + 1][j] == str(heir + 1):
                        newKingdom[i + 1][j] = str(heir)
                    if kingdom[i][j - 1] == str(heir + 1):
                        newKingdom[i][j - 1] = str(heir)
                    newKingdom[i][j] = str(heir)

    return newKingdom


def drawKingdom(kingdom):
    pass


def main():
    setup = input()
    while setup != "0 0 0 0":
        numbers = setup.split(" ")
        numHeirs = int(numbers[0])
        numRows = int(numbers[1])
        numCols = int(numbers[2])
        numBattles = int(numbers[3])
        kingdom = []
        for i in range(numRows):
            row = input().split(" ")
            kingdom.append(row)

        print(kingdom)
        #for i in range(numBattles):
        kingdom = simulateBattle(kingdom, numHeirs, numRows, numCols)

        print(kingdom)

        #drawKingdom(kingdom)

        setup = input()



main()