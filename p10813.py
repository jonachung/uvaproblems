def solve(card, numbers):
    count = 1
    for k in range(len(numbers)):
        for i in range(len(card)):
            cardLine = card[i]
            for j in range(len(cardLine)):
                    if int(numbers[k]) == int(cardLine[j]):
                        card[i][j] = "0"
                        if hasWinningCards(card):
                            print("BINGO after " + str(count) + " numbers announced")
                            return

        count += 1


def hasWinningCards(card):
    if card[0][0] == card[1][0] == card[2][0] == card[3][0] == card[4][0] == "0":
        return True
    elif card[0][1] == card[1][1] == card[2][1] == card[3][1] == card[4][1] == "0":
        return True
    elif card[0][2] == card[1][2] == card[3][2] == card[4][2] == "0":
        return True
    elif card[0][3] == card[1][3] == card[2][2] == card[3][3] == card[4][3] == "0":
        return True
    elif card[0][4] == card[1][4] == card[2][3] == card[3][4] == card[4][4] == "0":
        #print("I run")
        return True
    elif card[0][0] == card[0][1] == card[0][2] == card[0][3] == card[0][4] == "0":
        return True
    elif card[1][0] == card[1][1] == card[1][2] == card[1][3] == card[1][4] == "0":
        return True
    elif card[2][0] == card[2][1] == card[2][2] == card[2][3] == "0":
        return True
    elif card[3][0] == card[3][1] == card[3][2] == card[3][3] == card[3][4] == "0":
        return True
    elif card[4][0] == card[4][1] == card[4][2] == card[4][3] == card[4][4] == "0":
        return True
    elif card[0][0] == card[1][1] == card[3][3] == card[4][4] == "0":
        return True
    elif card[4][0] == card[3][1] == card[1][3] == card[0][4] == "0":
        return True

    return False


def main():
    numCards = int(input())
    #print(numCards)
    for i in range(numCards):
        #print("I happen")
        card = []
        for j in range(5):
            cardsLine = input().split()
            card.append(cardsLine)
        #print(card)

        numbers = []
        numberList = input()
        while len(numbers) < 75:
            numList = numberList.split()
            for k in range(len(numList)):
                numbers.append(numList[k])
            #print(len(numbers))
            if len(numbers) != 75:
                numberList = input()

        solve(card, numbers)


main()
