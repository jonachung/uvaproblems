def chunkString(string, length):
    listOfStrings = []
    for i in range(0, len(string), length):
        newString = string[i : length + i]
        listOfStrings.append(newString)

    return listOfStrings

def main():
    case = input()
    while case != "0":
        something = case.split(" ")
        number = int(something[0])
        string = something[1]
        lengthOfSubstring = int(len(string) / number)
        listOfSubstrings = chunkString(string, lengthOfSubstring)
        newListOfSubstrings = []
        for string in listOfSubstrings:
            reversedString = string[::-1]
            newListOfSubstrings.append(reversedString)

        outputString = ''.join(newListOfSubstrings)
        print(outputString)
        #print(listOfSubstrings)

        case = input()


main()

