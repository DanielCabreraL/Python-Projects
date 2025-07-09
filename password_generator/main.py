import password as pa

print("Welcome to the password generator!")
other_pass = "y"
while other_pass == "y":   
    long = pa.ask_length()
    numbers, cap_letters, sma_letters, spe_char, site = pa.conditions()
    password = pa.generator(numbers, cap_letters, sma_letters, spe_char, long, site)
    print(f"Your new password for {site} is: {password}")
    other_pass = pa.new_password()