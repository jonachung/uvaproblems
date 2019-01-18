def main():
    testCases = int(input())
    for case in range(testCases):
        numDays = int(input())
        calendar = []
        for day in range(numDays):
            calendar.append(False)
        numParties = int(input())
        for p in range(numParties):
            partyDay = int(input())
            calendar[partyDay - 1] = True
            for day in range(partyDay - 1, len(calendar), partyDay):
                calendar[day] = True

        count = 0
        for day in range(len(calendar)):
            if calendar[day] and day % 7 != 5 and day % 7 != 6:
                count += 1

        print(count)




main()