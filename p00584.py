def updateScore(scoreCard):
    scoreList = scoreCard.split()
    #print(score)
    i = 0
    frames = 0
    totalScore = 0
    while i < len(scoreList):
        temp = 0
        frames += 1
        if scoreList[i] == "X":
            if frames <= 10:
                temp += 10
                #print(temp)
                if scoreList[i + 2] == "/":
                    temp += 10
                    #print(temp)
                else:
                    if scoreList[i + 1] == "X":
                        temp += 10
                        #print(temp)
                    else:
                        temp += int(scoreList[i + 1])
                        #print(temp)

                    if scoreList[i + 2] == "X":
                        temp += 10
                        #print(temp)

                    else:
                        temp += int(scoreList[i + 2])
                        #print(temp)

            i += 1
        elif scoreList[i].isdigit():
            if i + 1 < len(scoreList) and frames <= 10:
                if scoreList[i + 1] == "/":
                    temp += 10
                    #print(temp)

                    if scoreList[i + 2] == "X":
                        temp += 10
                        #print(temp)

                    else:
                        temp += int(scoreList[i + 2])
                        #print(temp)

                else:
                    temp += (int(scoreList[i]) + int(scoreList[i + 1]))
                    #print(temp)

            i += 2
        totalScore += temp
        #print("totalScore " + str(totalScore))
    return totalScore



def main():
    scoreCard = input()
    while scoreCard != "Game Over":
        finalScore = 0
        finalScore = updateScore(scoreCard)
        print(finalScore)
        scoreCard = input()


main()