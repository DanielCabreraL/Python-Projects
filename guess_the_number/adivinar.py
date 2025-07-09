import random as ra

machine_choice = lambda : ra.randint(1,10)

def input_num():    
    
    while True:
        user_num = input("")
        try:
            user_num = int(user_num)
        except:
            print("Inválido, por favor, selecciona un número")
        else:
            break
    
    return user_num
 
def game(user_num, machine_num, attempts):

    if user_num == machine_num:
        print("¡Felicidades! Acertaste el número de la máquina, ¡Ganaste el juego!")
        print(f"La máquina pensó en el número {machine_num}")

    else:
        print("¡Casi! la máquina no pensó en ese número :(")
        if attempts != 0:
            print(f"Un intento más, te quedan {attempts} intentos, ingresa otro número: ")
            new_num = input_num()
            game(new_num, machine_num, attempts - 1)
        else:
            print(f"Perdiste, la máquina estaba pensando en el número {machine_num}")