def plus(n1,n2):
    result = n1+n2
    return result

def minus(n1,n2):
    result = n1-n2
    return result

def multiply(n1,n2):
    result = n1*n2
    return result

def divide(n1,n2):
    result = n1/n2
    return result

def is_even(r):
    if r % 2 == 0:
        r = "Result is even"
    else :
        r = "Result is odd"
    return r

def main():
    num1 = float(input("Enter your num1: "))
    num2 = float(input("Enter your num2: "))
    print("plus : + ")
    print("minus : - ")
    print("multiply : * ")
    print("divide : / ")
    symbol = input("Select your operator: ")

    if symbol == "+":
        result = plus(num1,num2)
    elif symbol == "-":
        result = minus(num1,num2)
    elif symbol == "*":
        result = multiply(num1,num2)
    elif symbol == "/":
        result = divide(num1,num2)
    
    even_or_odd = is_even(result)
    print(int(result))
    print(even_or_odd)

main()