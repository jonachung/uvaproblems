def main():
    numSoldiers = int(input())
    caseCount = 1
    while numSoldiers != 0:
        #print("Case " + str(caseCount) + ": ")
        total = 0
        for i in range(numSoldiers):
            soldier = input().split()
            tell = int(soldier[0])
            do = int(soldier[1])
            
            #print(tell)
            #print(do)

        numSoldiers = int(input())
        caseCount += 1



main()