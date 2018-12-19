def main():
    testCase = int(input())
    for i in range(0, testCase):
        if i != 0:
            print("")
        print("Hand #" + str(i + 1))
        numCards = int(input())
        count = 0
        totalPoints = 0
        for card in range(0, numCards):
            cardToCompare = input()
            card = cardsToCompare.split()[0]
            if cardToCompare == "fool" or cardToCompare == "twenty-one of trumps" or cardToCompare == "one of trumps":
                count = count + 1
                totalPoints = totalPoints + 4.5
            elif cardToCompare.split()[0] == "king":
                totalPoints = totalPoints + 4.5
            elif cardToCompare.split()[0] == "queen":
                totalPoints = totalPoints + 3.5
            elif cardToCompare.split()[0] == "knight":
                totalPoints = totalPoints + 2.5
            elif cardToCompare.split()[0] == "jack":
                totalPoints = totalPoints + 1.5
            else:
                totalPoints = totalPoints + 0.5
        if count == 0:
            totalPoints = totalPoints - 56
        elif count == 1:
            totalPoints = totalPoints - 51
        elif count == 2:
            totalPoints = totalPoints - 41
        elif count == 3:
            totalPoints = totalPoints - 36

        if totalPoints < 0:
            print("Game lost by " + str(int(abs(totalPoints))) + " point(s).")
        else:
            print("Game won by " + str(int(abs(totalPoints))) + " point(s).")

        #print("")


main()
