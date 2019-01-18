def main():
    startNum = int(input())
    caseNumber = 1
    while startNum >= 0:
        print("Case " + str(caseNumber) + ":")
        problemsCreated = input().split(" ")
        problemsNeeded = input().split(" ")
        totalProblems = startNum
        for problemMonth in range(len(problemsNeeded)):
            if totalProblems >= int(problemsNeeded[problemMonth]):
                print("No problem! :D")
                totalProblems -= int(problemsNeeded[problemMonth])
            else:
                print("No problem. :(")
            totalProblems += int(problemsCreated[problemMonth])
        caseNumber += 1


        startNum = int(input())


main()