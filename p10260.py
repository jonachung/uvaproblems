from sys import stdin


def in1Group(letter):
    if letter == "B" or letter == "F" or letter == "P" or letter == "V":
        return True


def in2Group(letter):
    if letter == "C" or letter == "G" or letter == "J" or letter == "K" or letter == "Q" or letter == "S" or letter == "X" or letter == "Z":
        return True


def in3Group(letter):
    if letter == "D" or letter == "T":
        return True


def in4Group(letter):
    return letter == "L"


def in5Group(letter):
    return letter == "M" or letter == "N"


def in6Group(letter):
    return letter == "R"


def main():
    for string in stdin:
        stringValue = ""
        letterValue = ""
        for letter in string:
            if len(stringValue) > 0:
                if in1Group(letter) != in1Group(letterValue[-1]) or in2Group(letter) != in2Group(letterValue[-1]) or in3Group(letter) != in3Group(letterValue[-1]) or in4Group(letter) != in4Group(letterValue[-1]) or in5Group(letter) != in5Group(letterValue[-1]) or in6Group(letter) != in6Group(letterValue[-1]):
                    if in1Group(letter):
                        stringValue += "1"
                    elif in2Group(letter):
                        stringValue += "2"
                    elif in3Group(letter):
                        stringValue += "3"
                    elif in4Group(letter):
                        stringValue += "4"
                    elif in5Group(letter):
                        stringValue += "5"
                    elif in6Group(letter):
                        stringValue += "6"
                    letterValue += letter
            else:
                if in1Group(letter):
                    stringValue += "1"
                elif in2Group(letter):
                    stringValue += "2"
                elif in3Group(letter):
                    stringValue += "3"
                elif in4Group(letter):
                    stringValue += "4"
                elif in5Group(letter):
                    stringValue += "5"
                elif in6Group(letter):
                    stringValue += "6"
                letterValue += letter
        print(stringValue)


main()
