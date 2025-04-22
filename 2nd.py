
if (chance ==5):
    print("You lost the game!!!")
    break
else:
    user=int(input("Guess the number between 0 to 100:"))
    if (user<num):
        print("Wrong!!!"+"Hint: Think little bit high number.")
        chance=chance + 1
        