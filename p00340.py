def main():
    testCase = 1
    length = int(input())
    while length != 0:
        secret = input().split()
        secret1 = list.copy(secret)
        print("Game " + str(testCase) + ":")
        while True:
            weak = 0
            strong = 0
            guess = input().split()
            if int(guess[0]) == 0:
                break
            for i in range(0, length):
                if int(secret[i]) == int(guess[i]):
                    strong = strong + 1
                    secret1[i] = 0
                    guess[i] = 0
            for i in range(0, length):
                if int(guess[i]) != 0:
                    for j in range(0, length):
                        if int(guess[i]) == int(secret1[j]):
                            weak = weak + 1
                            secret1[j] = 0
                            guess[i] = 0
                            break
            secret1 = list.copy(secret)
            print("    (" + str(strong) + "," + str(weak) + ")")
        length = int(input())
        testCase = testCase + 1


main()
