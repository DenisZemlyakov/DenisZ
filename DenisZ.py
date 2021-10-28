from random import choice
win = 0
loss = 0
tie = 0
rules = {'камень': 'бумага', 'ножницы': 'камень', 'бумага': 'ножницы'}
previous = ['камень', 'бумага', 'ножницы']
while True:
 human = input('камень, бумага, ножницы or Quit???: ')
 computer = rules[choice(previous)]  

if human in ('Quit'):
    print("YoU WoN %d TiMEs!" % win)
    print("yOu lOSt %d tImEs!" % loss)
    print("YoU TIeD %d TiMEs!" % tie)
    print("SeE YoU LaTeR!!! :)")

elif human in rules:
    previous.append(human)
    print('komp igraet', computer, end='; ')

    if rules[computer] == human:  
        print('WiN!')
        win += 1
    elif rules[human] == computer:  
        print('pc win!!!')
        loss += 1
    else:
        print("tIE!")
        tie += 1

else: print("that's not a valid choice")