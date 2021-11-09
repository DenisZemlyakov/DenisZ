import random
v1=choice(["kivi","käärid","paber"])
v2=choice(["kivi","käärid","paber"])
if m==1:
    while True:
        print("kas mängime? esc - valja, enter - mängime")
        if read_key()="esc":
            break
        elif read_key()=="enter" :
         p1=choice(v1)
         print("esimine bot: ",p1)
         p2=choice(v2)
         print("teine bot: ",p2)
         if p1==p2:
             print("viik")
        elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v[1 and p2==v2[2]:
         print("võitis 1")
        else:
        print("võtis2")     
comp = random.randint(1, 3)
if comp == 1:
        print("kivi.") 
if comp == 2:
        print("käärid.")
if comp == 3:
        print("paber.")
if p1 == p2:
        win = 0
if p1 == 1 and p2 == 2:
        win = 1 
if p1 == 1 and p2 == 3:
        win = 2 
if p1 == 2 and p2 == 1:
        win = 2  
if p1 == 2 and p2 == 3:
        win = 1 
if p1 == 3 and p2 == 1:
        win = 1
if p1 == 3 and p2 == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("ты Победил")
if win == 2:
        print("Победил компьютер!")

print()

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
print()
#..
from keyboard import*
from random import*
from den4ik modul import*
v1=["kivi","käärid","paaber"]
v2=["kivi","käärid","paaber"]
m=start()
if m==1:
				bot_vs_bot(v1,v2)
if m==2:
				while 1:
								pass
print()
#popitka
from keyboard import*
from random import*
from den4ik modul import*
def start():
    print("kivi,käärid,paber")
    m=3
    while m not in[1,2]:
        try:
            m=int(input("kellega mängime?\n1´-bootid \n2-robotiga"))
        except:
            ValueError
    return m
def bot_vs_bot(v1:list,v2:list):
    print("kas mängime? q - välja, enter -mängimise")
				if read_key()=="q":
								break
				elif read_key()=="enter":
								p1=choice(v1)
								print("Esimine bot: ",p1)
								p2=choice(v2)
								print("Teine bot:",p2)
								if p1==p2:
												print("viik")
								elif p1==v1[0] and p2==v2[1] or p1==v2[0] or p1==v1[1] and p2==v2[2]:
												print("võitist 1")
								else:
												print("võitist 2")