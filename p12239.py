def main():
    numbers = input()
    while numbers != "0 0":
        number = numbers.split()
        numBalls = int(number[0])
        remain = int(number[1])
        num = input().split()
        remainingNumbers = []
        mySet = set()
        for i in range(0, remain):
            n = num[i]
            remainingNumbers.append(int(n))

        for i in range(0, len(remainingNumbers)):
            for j in range(0, len(remainingNumbers)):
                temp = abs(remainingNumbers[i] - remainingNumbers[j])
                mySet.add(temp)

        if len(mySet) == numBalls + 1:
            print("Y")
        else:
            print("N")

        numbers = input()

main()
