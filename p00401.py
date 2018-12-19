def isPalidrome(string):
    reversedString = string[::-1]
    return reversedString == string


def isMirroredString(string):
    mirroredReference = {'E' : '3','J' : 'L', 'L' : 'J', 'S' : '2', '2' : 'S', '3' : 'E', '5' : 'Z'}
    mirroredString = ""
    for index in range(len(string)):
        if string[index] in mirroredReference:
            mirroredString += mirroredReference.get(string[index])
        else:
            mirroredString += string[index]
    reversedMirrorString = mirroredString[::-1]
    return reversedMirrorString == string


def main():
    string = input()
    while string != "":
        if isPalidrome(string):
            if isMirroredString(string):
                print(string + " -- is a mirrored palindrome.")
            else:
                print(string + " -- is a regular palindrome.")
        elif isMirroredString(string):
            print(string + " -- is a mirrored string.")
        else:
            print(string + " -- is not a palindrome.")
        print("")

        string = input()

main()