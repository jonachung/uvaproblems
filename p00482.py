def main():
    numCases = int(input())
    for case in range(numCases):
        if case > 0:
            print("")
        blankLine = input()
        firstList = input().split(" ")
        secondList = input().split(" ")

        for number in range(len(firstList)):
            if str(number + 1) in firstList:
                print(secondList[firstList.index(str(number + 1))])
        #print(firstList)
        #print(secondList)


main()