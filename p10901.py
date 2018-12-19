from collections import deque


def main():
    testCase = int(input())
    for i in range(testCase):
        numbers = input().split()
        carLimit = int(numbers[0])
        timeToCross = int(numbers[1])
        numCars = int(numbers[2])
        carsLeftBank = deque([])
        carsRightBank = deque([])
        for j in range(numCars):
            car = input().split()
            time = int(car[0])
            bank = car[1]
            if bank == "left":
                carsLeftBank.append(time)
            else:
                carsRightBank.append(time)

        findTimesCarsArrive(carLimit, carsLeftBank, carsRightBank, timeToCross)

        # print("Left")
        # for k in range(len(carsLeftBank)):
        #     print(carsLeftBank.popleft())
        #
        # print("Right")
        # for l in range(len(carsRightBank)):
        #     print(carsRightBank.popleft())
        #
        # print("Left again")
        # print(len(carsLeftBank))
        #
        # print("Right again")
        # print(len(carsRightBank))

        print("")


def findTimesCarsArrive(carLimit, carsLeftBank, carsRightBank, timeToCross):
    time = 0



main()