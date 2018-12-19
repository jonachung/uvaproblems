def getNewBoard(row):
    board = []
    for i in range(row):
        board.append([0] * row)
    return board


def isDuplicate(board, boards):
    for i in range(len(boards)):
        if boards[i] == board:
            return True
    return False


def printWinner(currentPlayer, currentMove):
    winner = 2 if currentPlayer == 1 else 1
    print("Player " + str(winner) + " wins on move " + str(currentMove))


def skipInputAndGetRow():
    move = input().split()
    while len(move) == 3:
        move = input().split()
    return move


def addNewPatterns(board, boards):
    b1 = rotate90D(board)
    boards.append(b1)
    b2 = rotate90D(b1)
    boards.append(b2)
    b3 = rotate90D(b2)
    boards.append(b3)
    b4 = rotate90D(b3)
    boards.append(b4)


def rotate90D(oldBoard):
    newBoard = getNewBoard(len(oldBoard))
    for row in range(len(oldBoard)):
        for col in range(len(oldBoard)):
            newBoard[row][col] = oldBoard[col][len(oldBoard) - 1 - row]
    return newBoard


def main():
    row = int(input())
    while row != 0:
        boards = []
        board = getNewBoard(row)
        currentPlayer = 1
        currentMove = 0
        completeOneGame = False
        move = input().split()
        while len(move) == 3:
            currentMove = currentMove + 1
            #print(currentMove)
            pieceRow = int(move[0])
            pieceCol = int(move[1])
            addOrRemove = move[2]
            board[pieceRow - 1][pieceCol - 1] = 1 if addOrRemove == "+" else 0
            #print(board)
            #print(boards)
            if isDuplicate(board, boards):
                printWinner(currentPlayer, currentMove)
                move = skipInputAndGetRow()
                completeOneGame = True
            else:
                if currentMove == 2 * row:
                    print("Draw")
                    move = skipInputAndGetRow()
                    completeOneGame = True
                else:
                    addNewPatterns(board, boards)
                    #print(boards)
                    currentPlayer = 2 if currentPlayer == 1 else 1
                    #print(board)
                    move = input().split()

            if completeOneGame:
                break # one game complete
            # continue the rest of one game
        # one game complete
        row = int(move[0])


main()