#x = 0
#for i in range(0,3):
#    x += i + 1
#print(x)

# n = int(input("Enter your num: "))
# print("multiplication table", n)
# for i in range(1,13):
#     print(f"{i} x {n} = {i*n}")


monster = 100
weapon1 = 5
weapon2 = 30
weapon3 = 7
while True:
    decide = int(input("You want to fight? (1 for fight) (2 for run): "))
    if decide == 1:
        round = int(input("How many round you gonna attack? : "))
        while monster != 0:
            for i in range(round):
                use = input("What weapon you gonna use(1 for 5 damage) (2 for 30 damage) (3 for 7 damage) : ")
                if monster > 0:
                    if "1" in use:
                        monster -= weapon1
                    elif "2" in use:
                        monster -= weapon2
                    else :
                        monster -= weapon3
                if monster < 0 :
                    round = round - (i+1)
                    break
                print("Now monster have Hp",monster)
            if monster < 0:
                print("monster have hp low than 0")
                print("monster have revive")
                print("monster have 20 Hp")
                monster = 20
            if monster == 0:
                print("monster die!")
                print("You won")
                break
            if monster > 0 and round == 0:
                print("You die!")
                break
        break
    else :
        print("You run away")
        break
print("Thank you for playing")