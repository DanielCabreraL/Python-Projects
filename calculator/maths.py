addition = lambda x, y: x + y                                                           #maths operators   
subtraction = lambda x, y: x - y
division = lambda x, y: x / y
multiplication = lambda x, y: x * y
potency = lambda x, y: x ** y

def menu():                                                                             #menu
    print("Select the calculation you want to make between both numbers:")
    print("1) Addtion")
    print("2) Substraction")
    print("3) Division")
    print("4) Multiplication")
    print("5) Potency of x to the y")
    print("0) Exit")

def calcs(num1, num2, selection):                                                       #menu operation
    print("------------------------------------------------------------------------")
    if selection == 1:
        print(f"Result of {num1} + {num2} = {addition(num1, num2)}")
    elif selection == 2:
        print(f"Result of {num1} - {num2} = {subtraction(num1, num2)}")
    elif selection == 3:
        print(f"Result of {num1} / {num2} = {division(num1, num2)}")
    elif selection == 4:
        print(f"Result of {num1} X {num2} = {multiplication(num1, num2)}")
    elif selection == 5:
        print(f"Result of {num1} ** {num2} = {potency(num1, num2)}")
    print("------------------------------------------------------------------------")

def input_num():                                                                        #input valid num
    while True:
        user_num = input("")
        try:
            user_num = int(user_num)
        except ValueError:
            print("Error: please select a integer number")
        else:
            break
    
    return user_num

def is_valid_option(num):                                                               #check if num is a valid option
    while num not in range(0,6):    
            print("Please, select a valid option: ")
            num = input_num()
    return num

def select_option():                                                                    #select option of menu
    selection = input_num()    
    selection_check = is_valid_option(selection)
    return selection_check