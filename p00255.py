from sys import stdin

from sys import stdin


def between(first, last, middle):
    if first < last:
        return middle >= first and middle <= last
    else:
        return middle >= last and middle <= first


def main():
    for line in stdin:
        moves = line.split()
        kingPosition = int(moves[0])
        queenPosition = int(moves[1])
        queenNewPosition = int(moves[2])

        kingRow = int(kingPosition / 8)
        #print("King Row " + str(kingRow))
        kingColumn = kingPosition % 8
        #rint("King Column " + str(kingColumn))

        queenRow = int(queenPosition / 8)
        #print("Queen Row " + str(queenRow))
        queenColumn = queenPosition % 8
        #print("Queen Column " + str(queenColumn))

        queenNewPositionRow = int(queenNewPosition / 8)
        #print("QueenNewPosition Row " + str(queenNewPositionRow))
        queenNewPositionColumn = queenNewPosition % 8
        #print("QueenNewPosition Column " + str(queenNewPositionColumn))

        if kingPosition == queenPosition:
            print("Illegal state")
        elif queenRow != queenNewPositionRow and queenColumn != queenNewPositionColumn:
            print("Illegal move")
        elif queenPosition == queenNewPosition:
            print("Illegal move")
        else:
            if (queenNewPositionRow == queenRow and kingRow == queenNewPositionRow
                and between(queenColumn, queenNewPositionColumn, kingColumn)) or (queenNewPositionColumn == queenColumn
                                                                                  and kingColumn == queenNewPositionColumn and between(
                        queenRow, queenNewPositionRow, kingRow)):
                print("Illegal move")
            elif ((kingRow == queenNewPositionRow and abs(kingColumn - queenNewPositionColumn) == 1) or (
                    kingColumn == queenNewPositionColumn and abs(kingRow - queenNewPositionRow) == 1)):
                print("Move not allowed")
            elif ((kingPosition == 0 and queenNewPosition == 9) or (kingPosition == 7 and queenNewPosition == 14) or (
                    kingPosition == 56 and queenNewPosition == 49) or (kingPosition == 63 and queenNewPosition == 54)):
                print("Stop")
            else:
                print("Continue")


main()
