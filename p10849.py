def main():
    testCase = int(input())
    for i in range(0, testCase):
        space = input()
        numCases = int(input())
        dimension = int(input())
        for i in range(0, numCases):
            positions = input().split()
            row1 = int(positions[0])
            col1 = int(positions[1])
            row2 = int(positions[2])
            col2 = int(positions[3])
            if row1 == row2 and col1 == col2:
                print("0")
            else:
                if (row1 + col1) % 2 != (row2 + col2) % 2: # one is 1 and one is 0
                    print("no move")
                else:
                    if row1 + col1 == row2 + col2:
                        print("1")
                    else:
                        print("2")


main()