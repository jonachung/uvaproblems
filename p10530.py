def main():
    num = int(input())
    while num != 0:
        upper = 10
        lower = 1

        result = input()
        while result != "right on":
            if result == "too high":
                upper = min(upper, num - 1)
            else:
                lower = max(lower, num + 1)
            num = int(input())
            result = input()

        if num >= lower and num <= upper:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        num = int(input())






main()
