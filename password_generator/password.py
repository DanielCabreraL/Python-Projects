import random as ra
import string as st

def valid_option(option):
    while option != 'y' and option != 'n':
        print("Please, enter a valid option (Y/N): ")
        option = input("").lower()
    return option

def input_length():                                                                        
    while True:
        user_num = input("")
        try:
            user_num = int(user_num)
        except ValueError:
            print("Error: please select a integer number")
        else:
            break
    
    return user_num

def ask_length():
    print("Please, enter the length of the new password (between 8 - 32): ")
    long = input_length()
    
    while long > 32 or long < 8:
        print("Please, select a number between 8 - 32")
        long = input_length()
    
    return long
    
def select_condition():
    cond = input("") 
    cond = cond.lower()
    cond = valid_option(cond)    
    return cond

def conditions():
    while True:
        print("Please, select at least one option (or specify details if it's the first prompt): ")
        print("Include numbers? (Y/N)")
        numbers = select_condition()
        print("Include capital letters? (Y/N)")
        cap_letters = select_condition()
        print("Include small letters? (Y/N)")
        sma_letters = select_condition()
        print("Include special characters? (Y/N)")
        spe_char = select_condition()
        print("Where do you use this password?")
        site = input("")
    
        if numbers == 'y' or cap_letters == 'y' or sma_letters == 'y' or spe_char == 'y':
            return numbers, cap_letters, sma_letters, spe_char, site
        else:
            print("You have not selected any character type. Please choose at least one.\n")

def choice_num():
    numbers = st.digits
    char = ra.choice(numbers)
    return char

def choice_small_lett():
    small_lett = st.ascii_lowercase
    char = ra.choice(small_lett)
    return char

def choice_cap_lett():
    capital_lett = st.ascii_uppercase
    char = ra.choice(capital_lett)
    return char

def choice_special_char():
    special_characters = st.punctuation
    char = ra.choice(special_characters)
    return char

def generator(num, cap, small, char, length, site):
    possible_chars = []
    
    #build possible chars
    if num == 'y':
        possible_chars += st.digits
    if small == 'y':
        possible_chars += st.ascii_lowercase
    if cap == 'y':
        possible_chars += st.ascii_uppercase
    if char == 'y':
        possible_chars += st.punctuation
    
    password = []
    
    #ensure at least one character of each type
    if num == 'y':
        password.append(choice_num())
    if small == 'y':
        password.append(choice_small_lett())
    if cap == 'y':
        password.append(choice_cap_lett())
    if char == 'y':
        password.append(choice_special_char())

    #complete the password
    for i in range(length - len(password)):
        password.append(ra.choice(possible_chars))
           
    #merge the characters
    ra.shuffle(password)
    passw = "".join(password)
         
    print(f"Password for '{site}' saved.")

    return passw

def new_password():
    print('Would you like to create a new password? (Y/N)')
    other_pass = input("")
    other_pass = valid_option(other_pass)
    return other_pass