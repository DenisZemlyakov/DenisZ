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

"""
Квадрат
=======
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.
"""
import math

def square(a):

    p = 4 * a
    s = a ** 2
    diag = a * math.sqrt(2)

    return p, s, diag