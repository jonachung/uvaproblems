def main():
    roundNumber = int(input())
    while roundNumber != -1:
        print("Round " + str(roundNumber))
        answer = input()
        guess = list(input())
        wrong = 0
        iter = 0
        while answer != "" and wrong <= 6 and iter < len(guess):
            if answer.find(guess[iter]) != -1:
                #print("Letter" + guess[iter])
                answer = answer.replace(guess[iter], '')
                #print(answer)
            else:
                #print("Letter" + guess[iter])
                wrong = wrong + 1
                #print("Wrong" + str(wrong))
            iter = iter + 1

        if answer == "":
            print("You win.")
        elif wrong == 7:
            print("You lose.")
        else:
            print("You chickened out.")

        roundNumber = int(input())


main()
