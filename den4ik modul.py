from keyboard import*
def start():
    """Teeme valik kellega mängime
    Tagastame m muutuja int formaadis
    :rtype: int
    """
    print("kivi,käärid,paber")
    m=3
    while m not in[1,2]:
        try:
            m=int(input("kellega mängime?\n1´-bootid \n2-robotiga"))
        except:
            ValueError
    return m

def bot_vs_bot(v1:list,v2:list):
    """Roobotitemäng
    Tagasime m muutuja int formaadis
    :parim lisst v1: järjend esimese roboti jaoks
    :param list v2 järjend teise roboti jaoks
    """
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
