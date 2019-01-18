def main():
    string = input()
    case = 1
    while string != "0 0 0":
        caseDetails = string.split(" ")
        row = int(caseDetails[0])
        col = int(caseDetails[1])
        numSetters = int(caseDetails[2])
        setterRows = set()
        setterCols = set()

        for s in range(numSetters):
            setter = input().split(" ")
            setterRow = int(setter[0])
            setterCol = int(setter[1])
            setterRows.add(setterRow)
            setterCols.add(setterCol)

        arif = input().split(" ")
        arifRow = int(arif[0])
        arifCol = int(arif[1])

        if (arifCol in setterCols and arifCol - 1 in setterCols and arifCol + 1 in setterCols) or (arifRow in setterRows
                                                                                                   and arifRow - 1 in setterRows and arifRow + 1 in setterRows):
            print("Case " + str(case) + ": Party time! Let's find a restaurant!")  # Arif can't escape
        else:
            print("Case " + str(case) + ": Escaped again! More 2D grid problems!")  # Arif can escape

        string = input()
        case += 1


main()
