import random

def turn_chip(chip):
    print(f"You {chip} chip")
    c = int(input("Choose your reward: "))
    print("Reward 1 use 3 chip : kfc")
    print("Reward 2 use 1 chip : milk ")
    print("Reward 3 use 1 chip : cookie")
    if c == 1 and chip-3 >= 0:
        print("You got kfc")
        c = c-3
    if c == 2 and chip-1 >= 0:
        print("You got milk")
        c = c-1
    if c == 3 and chip-1 >= 0:
        print("You got cookie")
        c = c-1

    game_choice(chip)

def guess_number(chip):
    print(f"Now you have chip {chip}")
    secret_number = random.randint(1, 10)
    turn = 3
    for i in range(3):
        print(f"Turn : {turn}")
        n = input("Guess your number : ")
        if n == secret_number:
            print("You won!!!")
            chip += 1
            game_choice(chip)
        else :
            print("Wrong!!!")
            print("HAHAHAHA")
        turn -= 1
    print("You lose (kak woi)")
    chip = chip - 1
    print(f"Now you have chip {chip}")
    game_choice(chip)

def black_jack(chip):
    ls =[]
    d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    dd = ['K','Q','J','10','9','8','7','6','5','4','3','2','A']
    print(f"Now you have chip {chip}")
    card = input("Enter all your card")
    ls= card.split(" ")
        
    message = d[ls[0]]+d[ls[1]] 
    if message <= 16:
        for j in range(2,5):
            message = message + d[ls[j]]
            if message > 16 :
                break
        if message > 21 :
            message = 'busted'
            
    for k in dd :
        if k in ls[0:j+1]:
            print(f"High Card is {k}")
            break 
            
    print(message)
    if message != "busted":
        print("You won")
        chip += 1
    else :
        print("You lose (kak woi)")
        chip -= 1
    print(f"Now you have chip {chip}")
    game_choice(chip)

def game_choice(chip):
    print(f"You have {chip} chip")
    print("[1] Blackjack")
    print("[2] Guess number")
    print("[3] Turn chip Reward")
    print("[4] Exit")
    choice = int(input("Select your games: "))
    if choice == 1:
        chip = black_jack(chip)
    if choice == 2:
        chip = guess_number(chip)
    if choice == 3:
        chip = turn_chip(chip)
    if choice == 4:
        return

def money():
    while True:
        m = int(input("Enter your money (100 baht = 1 chip) : "))
        if m % 100 == 0:
            chip = m//100
            return chip
        else:
            print("Plese enter value that can divide by 100")
    return

def main(user_age):
    if user_age >= 7:
        print("Welcome")
        chip = money()
        game_choice(chip)
        pass
    else :
        print("Too young")
        print("Get out!!!!")
    return

age = int(input("Enter your age: "))
main(age)

print("Thank you for playing :)")