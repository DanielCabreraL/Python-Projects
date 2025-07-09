import maths as ma

print("Insert the number one: ")
num1 = ma.input_num()
print("Insert the number two: ")
num2 = ma.input_num()

ma.menu()
selection_check = ma.select_option()

while selection_check != 0:
    ma.calcs(num1, num2, selection_check)
    ma.menu()
    selection_check = ma.select_option()
print("Closing calculator...")