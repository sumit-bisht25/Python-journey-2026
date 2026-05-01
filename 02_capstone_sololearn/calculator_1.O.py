print("welcome to nepali calculator.")

def calculator():
    num1 = float(input("oo shabji apni pehli number likho: "))
    num2 = float(input("oo shabji ab dusra bhi: "))
    
    operator = input("are ab +,-,*,/: chuno: ")
    
    if operator == "+":
        print("ye raha result saabji:", num1 + num2)
    elif operator == "-":
        print("ye raha result saabji:", num1 - num2)
    elif operator == "*":
        print("ye raha result saabji:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("ye rha result shabji:", num1 / num2)
        else:
            print("zero se divide ni ho sakta shabji")
    else:
        print("oo shabji dhang se chuno, boka shuda!")

# function ko call karo
 calculator () 