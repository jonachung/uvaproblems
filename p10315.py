from sys import stdin

def o(value):
    if value == "T":
        return 10
    elif value == "J":
        return 11
    elif value == "Q":
        return 12
    elif value == "K":
        return 13
    elif value == "A":
        return 14
    else:
        return int(value)


def check_is_consecutive(list1):
    for i in range(0, len(list1) - 1):
        diff = list1[i + 1] - list1[i]
        if diff != 1:
            return False
    return True


def checkStraightFlush(list1):
    if checkStraight(list1) and checkFlush(list1):
        return True
    else:
        return False


def compareStraightFlush(blackDeck, whiteDeck):
    win = compareHighCard(blackDeck, whiteDeck)
    if win == "Black":
        print("Black wins.")
    elif win == "White":
        print("White wins.")
    else:
        print("Tie.")


def checkFourOfAKind(list1):
    if list1[0][0] == list1[1][0] == list1[2][0] == list1[3][0]:
        return True
    elif list1[1][0] == list1[2][0] == list1[3][0] == list1[4][0]:
        return True
    else:
        return False


def compareFourOfAKind(blackDeck, whiteDeck):
    if o(blackDeck[0][0]) == o(blackDeck[1][0]) == o(blackDeck[2][0]) == o(blackDeck[3][0]):
        blackValue = o(blackDeck[0][0])
    elif o(blackDeck[1][0]) == o(blackDeck[2][0]) == o(blackDeck[3][0]) == o(blackDeck[4][0]):
        blackValue = o(blackDeck[1][0])
    if o(whiteDeck[0][0]) == o(whiteDeck[1][0]) == o(whiteDeck[2][0]) == o(whiteDeck[3][0]):
        whiteValue = o(whiteDeck[0][0])
    elif o(whiteDeck[1][0]) == o(whiteDeck[2][0]) == o(whiteDeck[3][0]) == o(whiteDeck[4][0]):
        whiteValue = o(whiteDeck[1][0])
    if blackValue > whiteValue:
        print("Black wins.")
    elif blackValue < whiteValue:
        print("White wins.")
    else:
        print("Tie.")


def checkFullHouse(list1):
    if o(list1[0][0]) == o(list1[1][0]) == o(list1[2][0]) and o(list1[3][0]) == o(list1[4][0]):
        return True;
    elif o(list1[0][0]) == o(list1[1][0]) and o(list1[2][0]) == o(list1[3][0]) == o(list1[4][0]):
        return True;
    else:
        return False;


def compareFullHouse(blackDeck, whiteDeck):
    if o(blackDeck[0][0]) == o(blackDeck[1][0]) == o(blackDeck[2][0]) and o(blackDeck[3][0]) == o(
            blackDeck[4][0]):
        blackValue = o(blackDeck[0][0])
    elif o(blackDeck[0][0]) == o(blackDeck[1][0]) and o(blackDeck[2][0]) == o(blackDeck[3][0]) == o(
            blackDeck[4][0]):
        blackValue = o(blackDeck[2][0])
    if o(whiteDeck[0][0]) == o(whiteDeck[1][0]) == o(whiteDeck[2][0]) and o(whiteDeck[3][0]) == o(
            whiteDeck[4][0]):
        whiteValue = o(whiteDeck[0][0])
    elif o(whiteDeck[0][0]) == o(whiteDeck[1][0]) and o(whiteDeck[2][0]) == o(whiteDeck[3][0]) == o(
            whiteDeck[4][0]):
        whiteValue = o(whiteDeck[2][0])

    if blackValue > whiteValue:
        print("Black wins.")
    elif blackValue < whiteValue:
        print("White wins.")
    else:
        print("Tie.")


def checkStraight(list1):
    valuesList = []
    for i in range(0, len(list1)):
        valuesList.append(o(list1[i][0]))
    return check_is_consecutive(valuesList)


def compareStraight(blackDeck, whiteDeck):
    win = compareHighCard(blackDeck, whiteDeck)
    if win == "Black":
        print("Black wins.")
    elif win == "White":
        print("White wins.")
    else:
        print("Tie.")


def checkThree(list1):
    if o(list1[0][0]) == o(list1[1][0]) == o(list1[2][0]):
        return True
    elif o(list1[1][0]) == o(list1[2][0]) == o(list1[3][0]):
        return True
    elif o(list1[2][0]) == o(list1[3][0]) == o(list1[4][0]):
        return True
    else:
        return False


def compareThree(blackDeck, whiteDeck):
    if o(blackDeck[0][0]) == o(blackDeck[1][0]) == o(blackDeck[2][0]):
        blackValue = o(blackDeck[0][0])
    elif o(blackDeck[1][0]) == o(blackDeck[2][0]) == o(blackDeck[3][0]):
        blackValue = o(blackDeck[1][0])
    elif o(blackDeck[2][0]) == o(blackDeck[3][0]) == o(blackDeck[4][0]):
        blackValue = o(blackDeck[2][0])
    if o(whiteDeck[0][0]) == o(whiteDeck[1][0]) == o(whiteDeck[2][0]):
        whiteValue = o(whiteDeck[0][0])
    elif o(whiteDeck[1][0]) == o(whiteDeck[2][0]) == o(whiteDeck[3][0]):
        whiteValue = o(whiteDeck[1][0])
    elif o(whiteDeck[2][0]) == o(whiteDeck[3][0]) == o(whiteDeck[4][0]):
        whiteValue = o(whiteDeck[2][0])
    if blackValue > whiteValue:
        print("Black wins.")
    elif blackValue < whiteValue:
        print("White wins.")
    else:
        print("Tie.")


def checkTwoPairs(list1):
    if o(list1[0][0]) == o(list1[1][0]) and o(list1[2][0]) == o(list1[3][0]):
        return True
    elif o(list1[1][0]) == o(list1[2][0]) and o(list1[3][0]) == o(list1[4][0]):
        return True
    else:
        return False


def compareTwoPairs(blackDeck, whiteDeck):
    if o(blackDeck[0][0]) == o(blackDeck[1][0]) and o(blackDeck[2][0]) == o(blackDeck[3][0]):
        if o(blackDeck[0][0]) > o(blackDeck[2][0]):
            maxBlackValue = o(blackDeck[0][0])
            secondBlackValue = o(blackDeck[2][0])
            blackRemainingCard = o(blackDeck[4][0])
        else:
            maxBlackValue = o(blackDeck[2][0])
            secondBlackValue = o(blackDeck[0][0])
            blackRemainingCard = o(blackDeck[4][0])
    elif o(blackDeck[1][0]) == o(blackDeck[2][0]) and o(blackDeck[3][0]) == o(blackDeck[4][0]):
        if o(blackDeck[1][0]) > o(blackDeck[3][0]):
            maxBlackValue = o(blackDeck[1][0])
            secondBlackValue = o(blackDeck[3][0])
            blackRemainingCard = o(blackDeck[0][0])
        else:
            maxBlackValue = o(blackDeck[3][0])
            secondBlackValue = o(blackDeck[1][0])
            blackRemainingCard = o(blackDeck[0][0])
    if o(whiteDeck[0][0]) == o(whiteDeck[1][0]) and o(whiteDeck[2][0]) == o(whiteDeck[3][0]):
        if o(whiteDeck[0][0]) > o(whiteDeck[2][0]):
            maxWhiteValue = o(whiteDeck[0][0])
            secondWhiteValue = o(whiteDeck[2][0])
            whiteRemainingCard = o(whiteDeck[4][0])
        else:
            maxWhiteValue = o(whiteDeck[2][0])
            secondWhiteValue = o(whiteDeck[0][0])
            whiteRemainingCard = o(whiteDeck[4][0])
    elif o(whiteDeck[1][0]) == o(whiteDeck[2][0]) and o(whiteDeck[3][0]) == o(whiteDeck[4][0]):
        if o(whiteDeck[1][0]) > o(whiteDeck[3][0]):
            maxWhiteValue = o(whiteDeck[1][0])
            secondWhiteValue = o(whiteDeck[3][0])
            whiteRemainingCard = o(whiteDeck[0][0])
        else:
            maxWhiteValue = o(whiteDeck[3][0])
            secondWhiteValue = o(whiteDeck[1][0])
            whiteRemainingCard = o(whiteDeck[0][0])

    #print("Max Black " + str(maxBlackValue))
    #print("Second Black " + str(secondBlackValue))
    #print("Black remaining " + str(blackRemainingCard))
    #print("Max white " + str(maxWhiteValue))
    #print("Second White " + str(secondWhiteValue))
    #print("White Remaining " + str(whiteRemainingCard))

    if maxBlackValue > maxWhiteValue:
        print("Black wins.")
    elif maxBlackValue < maxWhiteValue:
        print("White wins.")
    else:
        if secondBlackValue > secondWhiteValue:
            print("Black wins.")
        elif secondBlackValue < secondWhiteValue:
            print("White wins.")
        else:
            if blackRemainingCard > whiteRemainingCard:
                # print("I Happened")
                print("Black wins.")
            elif blackRemainingCard < whiteRemainingCard:
                print("White wins.")
            else:
                print("Tie.")


def checkPair(list1):
    if o(list1[0][0]) == o(list1[1][0]):
        return True
    elif o(list1[1][0]) == o(list1[2][0]):
        return True
    elif o(list1[2][0]) == o(list1[3][0]):
        return True
    elif o(list1[3][0]) == o(list1[4][0]):
        return True
    else:
        return False


def comparePair(blackDeck, whiteDeck):
    if o(blackDeck[0][0]) == o(blackDeck[1][0]):
        blackValue = o(blackDeck[0][0])
    elif o(blackDeck[1][0]) == o(blackDeck[2][0]):
        blackValue = o(blackDeck[1][0])
    elif o(blackDeck[2][0]) == o(blackDeck[3][0]):
        blackValue = o(blackDeck[2][0])
    elif o(blackDeck[3][0]) == o(blackDeck[4][0]):
        blackValue = o(blackDeck[3][0])
    if o(whiteDeck[0][0]) == o(whiteDeck[1][0]):
        whiteValue = o(whiteDeck[0][0])
    elif o(whiteDeck[1][0]) == o(whiteDeck[2][0]):
        whiteValue = o(whiteDeck[1][0])
    elif o(whiteDeck[2][0]) == o(whiteDeck[3][0]):
        whiteValue = o(whiteDeck[2][0])
    elif o(whiteDeck[3][0]) == o(whiteDeck[4][0]):
        whiteValue = o(whiteDeck[3][0])

    #print(blackValue)
    #print(whiteValue)

    if blackValue > whiteValue:
        print("Black wins.")
    elif blackValue < whiteValue:
        print("White wins.")
    else:
        newWhiteDeck = whiteDeck.copy()
        newBlackDeck = blackDeck.copy()
        if o(blackDeck[0][0]) == o(blackDeck[1][0]):
            newBlackDeck.remove(blackDeck[0])
            newBlackDeck.remove(blackDeck[1])
        elif o(blackDeck[1][0]) == o(blackDeck[2][0]):
            newBlackDeck.remove(blackDeck[1])
            newBlackDeck.remove(blackDeck[2])
        elif o(blackDeck[2][0]) == o(blackDeck[3][0]):
            #print(newBlackDeck[2])
            #print(newBlackDeck[3])
            newBlackDeck.remove(blackDeck[2])
            #print(newBlackDeck)
            newBlackDeck.remove(blackDeck[3])
        elif o(blackDeck[3][0]) == o(blackDeck[4][0]):
            newBlackDeck.remove(blackDeck[3])
            newBlackDeck.remove(blackDeck[4])
        if o(whiteDeck[0][0]) == o(whiteDeck[1][0]):
            newWhiteDeck.remove(whiteDeck[0])
            newWhiteDeck.remove(whiteDeck[1])
        elif o(whiteDeck[1][0]) == o(whiteDeck[2][0]):
            newWhiteDeck.remove(whiteDeck[1])
            newWhiteDeck.remove(whiteDeck[2])
        elif o(whiteDeck[2][0]) == o(whiteDeck[3][0]):
            newWhiteDeck.remove(whiteDeck[2])
            newWhiteDeck.remove(whiteDeck[3])
        elif o(whiteDeck[3][0]) == o(whiteDeck[4][0]):
            newWhiteDeck.remove(whiteDeck[3])
            newWhiteDeck.remove(whiteDeck[4])

        #print(newBlackDeck)
        #print(newWhiteDeck)

        if compareHighCard(newBlackDeck, newWhiteDeck) == "Black":
            print("Black wins.")
        elif compareHighCard(newBlackDeck, newWhiteDeck) == "White":
            print("White wins.")
        elif compareHighCard(newBlackDeck, newWhiteDeck) == "Tie":
            print("Tie.")


def compareHighCard(blackDeck, whiteDeck):
    win = " "
    blackValues = []
    whiteValues = []
    for i in range(0, len(blackDeck)):
        blackValues.append(o(blackDeck[i][0]))
    for i in range(0, len(whiteDeck)):
        whiteValues.append(o(whiteDeck[i][0]))
    while win != "Black" and win != "White" and win != "Tie":
        if len(blackValues) != 0 and len(whiteValues) != 0:
            blackMax = max(blackValues)
            whiteMax = max(whiteValues)
            if blackMax > whiteMax:
                win = "Black"
            elif blackMax < whiteMax:
                win = "White"
            elif blackMax == whiteMax:
                blackValues.remove(blackMax)
                whiteValues.remove(whiteMax)
        else:
            win = "Tie"
    return win


def checkFlush(list1):
    suit = list1[0][1]
    for i in range(0, len(list1)):
        if list1[i][1] != suit:
            return False;
    return True;


def compareFlush(blackDeck, whiteDeck):
    win = compareHighCard(blackDeck, whiteDeck)
    if win == "Black":
        print("Black wins.")
    elif win == "White":
        print("White wins.")
    else:
        print("Tie")

def custom_key(word):
    if word[0] == "A":
        return 14
    elif word[0] == "K":
        return 13
    elif word[0] == "Q":
        return 12
    elif word[0] == "J":
        return 11
    elif word[0] == "T":
        return 10
    else:
        return int(word[0])



def main():
    # line = input()
    # print(line)
    for line in stdin:
        hands = line.split()
        blackDeck = []
        whiteDeck = []
        #print(hands)
        for i in range(0, 5):
            blackDeck.append(hands[i])
        for i in range(5, len(hands)):
            whiteDeck.append(hands[i])

        blackDeck = sorted(blackDeck, key=custom_key)
        whiteDeck = sorted(whiteDeck, key=custom_key)

        #print(blackDeck)
        #print(whiteDeck)

        solve(blackDeck, whiteDeck)

        # line = input()
        # print(line)


def solve(blackDeck, whiteDeck):
    isBlackFlush = checkStraightFlush(blackDeck)
    isWhiteFlush = checkStraightFlush(whiteDeck)
    if isBlackFlush and isWhiteFlush:
        compareStraightFlush(blackDeck, whiteDeck)
        #print("StraightFlush")
        return
    else:
        if isBlackFlush:
            print("Black wins.")
            #print("BlackStraightFlush")
            return
        elif isWhiteFlush:
            print("White wins.")
            #print("whiteStraightFlush")
            return
    isBlackFourOfAKind = checkFourOfAKind(blackDeck)
    isWhiteFourOfAKind = checkFourOfAKind(whiteDeck)
    if isBlackFourOfAKind and isWhiteFourOfAKind:
        compareFourOfAKind(blackDeck, whiteDeck)
        #print("fourofakind")
        return
    else:
        if isBlackFourOfAKind:
            print("Black wins.")
            #print("blackfourofakind")
            return
        elif isWhiteFourOfAKind:
            print("White wins.")
            #print("whitefourofakind")
            return
    isBlackFullHouse = checkFullHouse(blackDeck)
    isWhiteFullHouse = checkFullHouse(whiteDeck)
    if isBlackFullHouse and isWhiteFullHouse:
        # print("Works")
        compareFullHouse(blackDeck, whiteDeck)
        #print("fullhouse")
        return
    else:
        # print("Works 2")
        if isBlackFullHouse:
            print("Black wins.")
            #print("blackfullhouse")
            return
        elif isWhiteFullHouse:
            print("White wins.")
            #print("whitefullhouse")
            return
    isBlackFlush = checkFlush(blackDeck)
    isWhiteFlush = checkFlush(whiteDeck)
    if isBlackFlush and isWhiteFlush:
        compareFlush(blackDeck, whiteDeck)
        #print("flush")
        return
    else:
        if isBlackFlush:
            print("Black wins.")
            #print("blackflush")
            return
        elif isWhiteFlush:
            print("White wins.")
            #print("whiteflush")
            return
    isBlackStraight = checkStraight(blackDeck)
    isWhiteStraight = checkStraight(whiteDeck)
    if isBlackStraight and isWhiteStraight:
        compareStraight(blackDeck, whiteDeck)
        #print("straight")
        return
    else:
        if isBlackStraight:
            print("Black wins.")
            #print("blackstraight")
            return
        elif isWhiteStraight:
            print("White wins.")
            #print("whitestraight")
            return
    isBlackThree = checkThree(blackDeck)
    isWhiteThree = checkThree(whiteDeck)
    if isBlackThree and isWhiteThree:
        compareThree(blackDeck, whiteDeck)
        #print("three")
        return
    else:
        if isBlackThree:
            print("Black wins.")
            #print("blackthree")
            return
        elif isWhiteThree:
            print("White wins.")
            #print("whitethree")
            return
    isBlackTwoPairs = checkTwoPairs(blackDeck)
    isWhiteTwoPairs = checkTwoPairs(whiteDeck)
    #print(isBlackTwoPairs)
    #print(isWhiteTwoPairs)
    if isBlackTwoPairs and isWhiteTwoPairs:
        compareTwoPairs(blackDeck, whiteDeck)
        #print("two pair")
        return
    else:
        if isBlackTwoPairs:
            print("Black wins.")
            #print("blacktwopair")
            return
        elif isWhiteTwoPairs:
            print("White wins.")
            #print("whitetwopair")
            return
    isBlackPair = checkPair(blackDeck)
    isWhitePair = checkPair(whiteDeck)
    if isBlackPair and isWhitePair:
        comparePair(blackDeck, whiteDeck)
        #print("pair")
        return
    else:
        if isBlackPair:
            print("Black wins.")
            #print("blackpair")
            return
        elif isWhitePair:
            print("White wins.")
            #print("whitepair")
            return
    hand = compareHighCard(blackDeck, whiteDeck)
    if hand == "Black":
        print("Black wins.")
        #print("blackhighcard")
        return
    elif hand == "White":
        print("White wins.")
        #print("whitehighcard")
        return
    else:
        print("Tie.")
        #print("tiehighcard")
        return


main()
