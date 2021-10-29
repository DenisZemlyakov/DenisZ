import random
ver = 0
while (ver == 0):
        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
if player == 1:
        print("камень.")  
if player == 2:
        print("ножницы.") 
if player == 3:
        print("бумагу.")  
comp = random.randint(1, 3)
if comp == 1:
        print("Компьютер выбрал камень.") 
if comp == 2:
        print("Компьютер выбрал ножницы.")
if comp == 3:
        print("Компьютер выбрал бумагу.")
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2 
if player == 2 and comp == 1:
        win = 2  
if player == 2 and comp == 3:
        win = 1 
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("ты Победил")
if win == 2:
        print("Победил компьютер!")