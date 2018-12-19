def isPalindrome(string):
    punctuation = [".", ",", "!", "?", " "]
    newString = ""
    for index in range(len(string)):
        if string[index] not in punctuation:
            character = string[index].lower()
            newString += character

    reverseNewString = newString[::-1]
    return reverseNewString == newString


def main():
    string = input()
    while string != "DONE":
        if isPalindrome(string):
            print("You won't be eaten!")
        else:
            print("Uh oh..")

        string = input()

main()