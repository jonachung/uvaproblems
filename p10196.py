def readInputToArray():
    board = []
    for row in range(0, 8):
        line = list(input())
        if not line:
            line = list(input())
        #print(line)
        board.append(line)
    return board


def checkBlackPawn(row, col, kRow, kCol, board):
    king = board[kRow][kCol]
    #print(king)
    #print("King Row " + str(kRow)) # 0
    #print("King Col " + str(kCol)) # 2
    #print("Pawn Row " + str(row)) # 1
    #print("Pawn Col " + str(col)) # 1
    # if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == king:
    #     return True
    # elif row - 1 >= 0 and col + 1 < 8 and board[row - 1][col + 1] == king:
    #     return True
    # else:
    #     return False

    if row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1] == king:
        return True
    elif row + 1 < 8 and col + 1 < 8 and board[row + 1][col + 1] == king:
        return True
    else:
        return False


def checkWhitePawn(row, col, kRow, kCol, board):
    king = board[kRow][kCol]
    # if row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1] == king:
    #     return True
    # elif row + 1 < 8 and col + 1 < 8 and board[row + 1][col + 1] == king:
    #     return True
    # else:
    #     return False

    if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == king:
        return True
    elif row - 1 >= 0 and col + 1 < 8 and board[row - 1][col + 1] == king:
        return True
    else:
        return False


def checkRook(row, col, kRow, kCol, board):
    if row != kRow and col != kCol:
        return False
    for x in range(row + 1, 8):
        if board[x][col] == board[kRow][kCol]:
            return True
        elif board[x][col].isalpha() and board[x][col] != board[kRow][kCol]:
            break
    for x in range(row - 1, -1, -1):
        if board[x][col] == board[kRow][kCol]:
            return True
        elif board[x][col].isalpha() and board[x][col] != board[kRow][kCol]:
            break
    for x in range(col + 1, 8):
        if board[row][x] == board[kRow][kCol]:
            return True
        elif board[row][x].isalpha() and board[row][x] != board[kRow][kCol]:
            break
    for x in range(col - 1, -1, -1):
        if board[row][x] == board[kRow][kCol]:
            return True
        elif board[row][x].isalpha() and board[row][x] != board[kRow][kCol]:
            break
    return False


def checkKnight(row, col, board, kRow, kCol):
    king = board[kRow][kCol]
    if row - 2 >= 0 and col - 1 >= 0 and board[row - 2][col - 1] == king:
        return True
    elif row - 1 >= 0 and col - 2 >= 0 and board[row - 1][col - 2] == king:
        return True
    elif row + 1 < 8 and col - 2 >= 0 and board[row + 1][col - 2] == king:
        return True
    elif row + 2 < 8 and col - 1 >= 0 and board[row + 2][col - 1] == king:
        return True
    elif row + 1 < 8 and col + 2 < 8 and board[row + 1][col + 2] == king:
        return True
    elif row + 2 < 8 and col + 1 < 8 and board[row + 2][col + 1] == king:
        return True
    elif row - 1 >= 0 and col + 2 < 8 and board[row - 1][col + 2] == king:
        return True
    elif row - 2 >= 0 and col + 1 < 8 and board[row - 2][col + 1] == king:
        return True
    else:
        return False


def checkBishop(row, col, board, kRow, kCol):
    #print("King row " + str(kRow) + " King col " + str(kCol))
    if abs(row - kRow) - abs(col - kCol) != 0:
        #print("Printed False")
        return False
    for i in range(1, 8):
        newRow = row - i
        newCol = col - i
        #print("Row " + str(newRow) + " Col " + str(newCol))
        if newRow < 8 and newCol < 8 and newRow >= 0 and newCol >= 0:
            #print("Ipassed")
            if board[newRow][newCol] == board[kRow][kCol]:
                #print("True")
                return True
            elif board[newRow][newCol].isalpha() and board[newRow][newCol] != board[kRow][kCol]:
                break
    for i in range(1, 8):
        newRow = row - i
        newCol = col + i
        #print("Row " + str(newRow) + " Col " + str(newCol))
        if newRow < 8 and newCol < 8 and newRow >= 0 and newCol >= 0:
            #print("Ipassed")
            if board[newRow][newCol] == board[kRow][kCol]:
                #print("True")
                return True
            elif board[newRow][newCol].isalpha() and board[newRow][newCol] != board[kRow][kCol]:
                break
    for i in range(1, 8):
        newRow = row + i
        newCol = col - i
        #print("Row " + str(newRow) + " Col " + str(newCol))
        if newRow < 8 and newCol < 8 and newRow >= 0 and newCol >= 0:
            #print("Ipassed")
            if board[newRow][newCol] == board[kRow][kCol]:
                #print("True")
                return True
            elif board[newRow][newCol].isalpha() and board[newRow][newCol] != board[kRow][kCol]:
                break
    for i in range(1, 8):
        newRow = row + i
        newCol = col + i
        #print("Row " + str(newRow) + " Col " + str(newCol))
        if newRow < 8 and newCol < 8 and newRow >= 0 and newCol >= 0:
            #print("Ipassed")
            if board[newRow][newCol] == board[kRow][kCol]:
                #print("True")
                return True
            elif board[newRow][newCol].isalpha() and board[newRow][newCol] != board[kRow][kCol]:
                break
    #print("Printed False 1")
    return False


def checkQueen(row, col, kRow, kCol, board):
    if checkBishop(row, col, board, kRow, kCol) or checkRook(row, col, kRow, kCol, board):
        return True
    return False


def isKingUnderAttack(row, col, board, blackRow, blackCol, whiteRow, whiteCol):
    if board[row][col] == "p":
        #print("Compare b pawn")
        if checkBlackPawn(row, col, whiteRow, whiteCol, board):
            #print("Pawn to Black")
            return "White"
    elif board[row][col] == "P":
        #print("Compare w pawn")
        if checkWhitePawn(row, col, blackRow, blackCol, board):
            #print("Pawn to White")
            return "Black"
    elif board[row][col] == "r" or board[row][col] == "R":
        if board[row][col] == "r":
            #print("Compare b rook")
            if checkRook(row, col, whiteRow, whiteCol, board):
                #print("Rook to Black")
                return "White"
        else:
            #print("Compare w rook")
            if checkRook(row, col, blackRow, blackCol, board):
                #print("Rook to White")
                return "Black"
    elif board[row][col] == "n" or board[row][col] == "N":
        if board[row][col] == "n":
            #print("Compare b knight")
            if checkKnight(row, col, board, whiteRow, whiteCol):
                #print("Knight to Black")
                return "White"
        else:
            #print("Compare w knight")
            if checkKnight(row, col, board, blackRow, blackCol):
                #print("Knight to WHite")
                return "Black"
    elif board[row][col] == "b" or board[row][col] == "B":
        if board[row][col] == "b":
            #print("Compare b bishop")
            if checkBishop(row, col, board, whiteRow, whiteCol):
                #print("Bishop to Black")
                return "White"
        else:
            #print("Compare w bishop")
            if checkBishop(row, col, board, blackRow, blackCol):
                #print("Bishop to WHite")
                return "Black"
    elif board[row][col] == "q" or board[row][col] == "Q":
        if board[row][col] == "q":
            #print("Compare b queen")
            if checkQueen(row, col, whiteRow, whiteCol, board):
                #print("Queen to Black")
                return "White"
        else:
            #print("Compare w queen")
            if checkQueen(row, col, blackRow, blackCol, board):
                #print("Queen to WHite")
                return "Black"
    elif board[row][col] == ".":
        #print("Compare Empty Space")
        return None

    return None


def findKings(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "k":
                blackKingRow = row
                blackKingCol = col
            elif board[row][col] == "K":
                whiteKingCol = col
                whiteKingRow = row
    return blackKingRow, blackKingCol, whiteKingRow, whiteKingCol


def solve(board, blackRow, blackCol, whiteRow, whiteCol):
    for row in range(len(board)):
        #print("Row " + str(row))
        for col in range(len(board[row])):
            #print("Row " + str(row) + " Col " + str(col))
            if board[row][col] != "k" and board[row][col] != "K":
                color = isKingUnderAttack(row, col, board, blackRow, blackCol, whiteRow, whiteCol)
                if color is not None:
                    return color


def printResult(color, testCase):
    if color == "Black":
        print("Game #" + str(testCase) + ": black king is in check.")
    elif color == "White":
        print("Game #" + str(testCase) + ": white king is in check.")
    else:
        print("Game #" + str(testCase) + ": no king is in check.")


def main():
    testCase = 1
    board = readInputToArray()
    empty = [["." for j in range(8)] for i in range(8)]
    #print(empty)
    while board != empty:
        #print(board)
        blackKingRow, blackKingCol, whiteKingRow, whiteKingCol = findKings(board)
        color = solve(board, blackKingRow, blackKingCol, whiteKingRow, whiteKingCol)
        printResult(color, testCase)
        board = readInputToArray()
        testCase = testCase + 1


main()
