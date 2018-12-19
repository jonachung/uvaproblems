def main():
    numbers = input()
    while numbers != "":
        numList = numbers.split()
        differenceSet = set()
        if len(numList) == 1:
            print("Not jolly")
        for i in range(len(numList) - 1):
            difference = abs(int(numList[i]) - int(numList[i + 1]))
            if len(numList) > difference >= 1:
                differenceSet.add(numList[i])
        if len(differenceSet) == len(numList) - 1:
            print("Jolly")
        else:
            print("Not jolly")
        numbers = input()


main()