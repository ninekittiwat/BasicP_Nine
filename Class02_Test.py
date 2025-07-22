distance = int(input("Enter your distance(km.) : "))
if distance > 500 :
    cost = 45
elif distance > 300 :
    cost = 35
elif distance > 100 :
    cost = 25
elif distance > 50 :
    cost = 15
elif distance > 4 :
    cost = 10
else:
    cost = 0
print(cost)