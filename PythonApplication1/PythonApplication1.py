from myyymodule1 import*
while True:
				print("funktsioonid".center(50,"+"))
				v=input("arithmetic- A")
				if v.upper()=="A":
								arv1=float(input("Arv 1:"))
								arv2=float(input("Arv 2:"))
								sym=input("Tehe:")
								rezult=arithmetic(arv1,arv2,sym)
								print(rezult)
from myyymodule1 import*
print()
while True:
				print("funktsioonid".center(50,"+"))
				v=input("arithmetic- A,\nis_year_leap-Y")
				v=input()
				if v.upper()=="A":
								arv1=float(input("Arv 1:"))
								arv2=float(input("Arv 2:"))
								sym=input("Tehe:")
								rezult=arithmetic(arv1,arv2,sym)
								print(rezult)
				elif v.upper()=="Y":
								rezult=is_year_leap(int(input("Sisesta aasta")))
print()
def season(moth):
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"
month = input("Sisestage kuus(число):")
while True:
    if not month.isdigit():
        print("Sisendi viga!")
        print("Kasutage ainult täisarve.")
        month = input("Sisestage kuus(число):")
        continue
    else:
        break
month = int(month)
while True:
    if month == 0:
        print("Sellist kuud ei ole olemas")
        print("Kasutage ainult täisarve.")
        month = input("Введите месяц(число):")
        continue
    else:
        break
month = int(month)
answer = season(month)
print(answer)
