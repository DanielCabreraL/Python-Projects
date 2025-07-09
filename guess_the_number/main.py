import adivinar as ad

print("La máquina está pensando un número del 1 al 10, tenés que adivinar cuál número está pensando")
print("¿Cuál es el número que está pensando?")
num_user = ad.input_num()
num_machine = ad.machine_choice()
ad.game(num_user, num_machine, 2)