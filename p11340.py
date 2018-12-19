def main():
    testCase = int(input())
    for i in range(testCase):
        numCharacters = int(input())
        priceOfCharacters = {}
        for j in range(numCharacters):
            letterAndPrice = input().split()
            letter = letterAndPrice[0]
            price = int(letterAndPrice[1])
            priceOfCharacters[letter] = price
        #print(priceOfCharacters)
        numLines = int(input())
        totalPrice = 0
        for k in range(numLines):
            line = list(input())
            for i in range(len(line)):
                if line[i] in priceOfCharacters:
                    totalPrice += priceOfCharacters.get(line[i])
        price = str(totalPrice / 100) + "$"
        print(price)

            #print(line)


main()