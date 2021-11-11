def arithmetic(a: float,b:float,c:str):
				"""Lihtne kalkulaator
				+ - liitmine
				- - lahutamine
				* - korrutamine
				/ - jagamine
				:param float a: Esimene arv
				:param float b: Teine arv
				:param str c:Aritmeetiline tehing
				:rtype float:
				"""
				if c=="+":
								r=a+b
				elif c=="-":
								r=a-b
				elif c=="*":
								r=a*b
				elif c=="/":
								if b!=0:
												r=a/b
								else:
												print("Div0")
				else:
								print("viga")
				return r
def is_year_leap(aasta: int):
				"""Liigaasta leidmine
				Tagastab true kui aasta on liigaasta ja false kui ei ole
				:param int Aasta number
				:rtype bool: Funktsioni vastus loogilises formaadis
				"""
				if aasta%4==0:
								vastus=True
				else:
								vastus=False
				return vastus

import math
def square(a):
    p = 4 * a
    s = a ** 2
    diag = a * math.sqrt(2)
    return p, s, diag

def season(moth):
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"
month = input("Введите месяц(число):")
while True:
    if not month.isdigit():
        print("Sisendi viga!")
        print("Kasutage ainult täisarve.")
        month = input("Введите месяц(число):")
        continue
    else:
        break
month = int(month)
while True:
    if month == 0:
        print("Такого месяца несуществует")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break
month = int(month)
answer = season(month)
print(answer)