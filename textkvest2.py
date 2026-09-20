from time import sleep
import random
import sys
import images

hods = 50  # количество ходов

def potratit_hod():
    global hods
    hods -= 1
    if hods <= 0:
        print('\nВремя вышло! Вы не успели выбраться из дома...')
        sleep(3)
        badkoncovka()
        sys.exit()
    else:
        sleep(1)

def komnata1():
    potratit_hod()
    print('ваши действия:\n1. осмотреться\n2. посмотреть ваш инвентарь\n3. перейти в следующую комнату')
    hod=input()
    if hod == '1':
        print('вы осмотрелись и увидели тумбочку, коробку с игрушками, письменный стол')
        sleep(3)
        hod=input('ваши действия:\n1. открыть тумбочку\n2. осмотреть коробку с игрушками\n3. осмотреть письменный стол\n')
        if hod=='1':
            komnata1tumbochka()
        elif hod=='2':
            komnata1korobka()
        elif hod=='3':
            komnata1stol()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata1()
    elif hod=='2':
        vivodinventarya(inventar,komnata1)
    elif hod=='3':
        print('вы зашли в другую комнату')
        sleep(3)
        komnata2()
    else:
        print('что-то непонятно, повторите пожалуйста!')
        sleep(2)
        komnata1()

def komnata2():
    potratit_hod()
    print('ваши действия:\n1. осмотреться\n2. посмотреть ваш инвентарь\n3. посмотреть есть-ли проходы в другие комнаты')
    hod=input()
    if hod == '1':
        print('вы осмотрелись и увидели\n1. диван\n2. шкаф\n3. тумбочку')
        sleep(3)
        hod=input()
        if hod=='1':
            komnata2divan()
        elif hod=='2':
            komnata2shkaf()
        elif hod=='3':
            komnata2tumbochka()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata2()
    elif hod=='2':
        vivodinventarya(inventar,komnata2)
    elif hod=='3':
        hod=input('вы находите 2 двери:\n1. дверь в комнату, где вы были в самом начале\n2. дверь в другую комнату\n')
        if hod=='1':
            print('вы заходите в комнату где начинали')
            sleep(3)
            komnata1()
        elif hod=='2':
            print('вы заходите в 3 комнату')
            sleep(3)
            komnata3()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata2()
    else:
        print('что-то непонятно, повторите пожалуйста!')
        sleep(2)
        komnata2()

def komnata3():
    potratit_hod()
    print('ваши действия\n1. осмотреться\n2. посмотреть инвентарь\n3. посмотреть есть-ли проходы в другие комнаты')
    hod=input()
    if hod=='1':
        hod=input('вы видите\n1. шкаф\n2. ковёр\n3. тумбочка\n')
        if hod=='1':
            komnata3shkaf()
        elif hod=='2':
            komnata3kover()
        elif hod=='3':
            komnata3tumbochka()
        else:
            print('что-то непонятно, повторите пожалуйста')
            sleep(2)
            komnata3()
    elif hod=='2':
        vivodinventarya(inventar,komnata3)
    elif hod=='3':
        hod=input('вы находите 3 двери:\n1. дверь из которой вы только что зашли\n2. новая дверь\n3. дверь похожая на входную, может быть это и есть выход\n')
        if hod=='1':
            komnata2()
        elif hod=='2':
            komnata4()
        elif hod=='3':
            if keykr in inventar:
                koncovka()
                sys.exit()
            else:
                print('У вас нету подходящего ключа')
                sleep(3)
                komnata3()
        else:
            print('что-то непонятно, повторите пожалуйста')
            sleep(2)
            komnata3()
    else:
        print('что-то непонятно, повторите пожалуйста')
        sleep(2)
        komnata3()

def komnata4():
    potratit_hod()
    print('ваши действия:\n1. осмотреться\n2. посмотреть ваш инвентарь\n3. посмотреть есть-ли проходы в другие комнаты')
    hod=input()
    if hod == '1':
        print('вы осмотрелись и увидели\n1. диван\n2. шкаф\n3. тумбочку')
        sleep(3)
        hod=input()
        if hod=='1':
            komnata4divan()
        elif hod=='2':
            komnata4shkaf()
        elif hod=='3':
            komnata4tumbochka()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata4()
    elif hod=='2':
        vivodinventarya(inventar,komnata4)
    elif hod=='3':
        hod=input('вы находите 2 двери и лестницу похожую на ведущую подвал:\n1. дверь в комнату, где вы были до этого\n2. дверь в другую комнату\n3. пойти на лестницу похожую на ведущую в подвал\n')
        if hod=='1':
            print('вы заходите в 3 комнату')
            sleep(3)
            komnata3()
        elif hod=='2':
            if keyjel in inventar:
                print('у вас есть подходящий ключ, вы заходите в спальню владельца')
                sleep(3)
                komnata6()
            else:
                print('У вас ещё нет нужного ключа')
                sleep(3)
                komnata4()
        elif hod=='3':
            if keysi in inventar:
                print('у вас есть ключ и поэтому вы открываете лестницу и спускаетесь в подвал')
                sleep(3)
                komnata5()
            else:
                print('чтобы открыть вход на лестницу найдите ключ')
                sleep(3)
                komnata4()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata4()
    else:
        print('что-то непонятно, повторите пожалуйста')
        sleep(2)
        komnata4()

def komnata5():
    potratit_hod()
    print('ваши действия:\n1. осмотреться\n2. посмотреть ваш инвентарь\n3. выйти из подвала')
    hod=input()
    if hod == '1':
        print('вы осмотрелись и увидели тумбочку, коробку с картошкой, письменный стол')
        sleep(3)
        hod=input('ваши действия:\n1. открыть тумбочку\n2. осмотреть коробку с картошкой\n3. осмотреть письменный стол\n')
        if hod=='1':
            komnata5tumbochka()
        elif hod=='2':
            komnata5korobka()
        elif hod=='3':
            komnata5stol()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata5()
    elif hod=='2':
        vivodinventarya(inventar,komnata5)
    elif hod=='3':
        print('вы вылезли из подвала')
        sleep(3)
        komnata4()
    else:
        print('что-то непонятно, повторите пожалуйста!')
        sleep(2)
        komnata5()

def komnata6():
    potratit_hod()
    print('ваши действия:\n1. осмотреться\n2. посмотреть ваш инвентарь\n3. выйти из спальни владельцев')
    hod=input()
    if hod == '1':
        print('вы осмотрелись и увидели шкаф, письменный стол, кровать, сейф')
        sleep(3)
        hod=input('ваши действия:\n1. посмотреть под шкафом\n2. осмотреть письменный стол\n3. осмотреть кровать\n4. попробовать открыть сейф\n')
        if hod=='1':
            komnata6shkaf()
        elif hod=='2':
            komnata6stol()
        elif hod=='3':
            komnata6krovat()
        elif hod=='4':
            komnata6seif()
        else:
            print('что-то непонятно, повторите пожалуйста!')
            sleep(2)
            komnata6()
    elif hod=='2':
        vivodinventarya(inventar,komnata6)
    elif hod=='3':
        print('вы вышли из спальни владельца')
        sleep(3)
        komnata4()
    else:
        print('что-то непонятно, повторите пожалуйста!')
        sleep(2)
        komnata6()

def koncovka():
    print('Вы выбираетесь из дома!!!')
    sleep(3)
    print('На улице вас встречает толпа народу, которая следила за вашими приключениями!')
    sleep(3)
    print('Ведущий квеста вручает вам золотой кубок "Лучший побег года" и сертификат на 100 000 рублей!')
    sleep(3)
    print('А ещё вы получаете десятку по биологии от Ирины Николаевны!')
    sleep(3)
    print('Поздравляем, вы прошли квест!')
    sleep(3)
    print(images.pobeda)
    sleep(3)
    print('КОНЕЦ!')
    

def badkoncovka():
    print('Вы проиграли!!!!')
    sleep(2)
    print('Вы не успели выбраться из дома за отведённое время...')
    sleep(3)
    print(images.lose)
    sleep(3)
    print('КОНЕЦ :(')
    sys.exit()

def komnata1tumbochka():
    potratit_hod()
    print('в тумбочке лежит -', komnatapred[0][0])
    sleep(2)
    if komnatapred[0][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[0][0])
        komnatapred[0][0]='ничего'
    komnata1()

def komnata1korobka():
    potratit_hod()
    print('в коробке с игрушками лежит -', komnatapred[0][1])
    sleep(2)
    if komnatapred[0][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[0][1])
        komnatapred[0][1]='ничего'
    komnata1()

def komnata1stol():
    potratit_hod()
    print('в столе лежит -', komnatapred[0][2])
    sleep(2)
    if komnatapred[0][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[0][2])
        komnatapred[0][2]='ничего'
    komnata1()

def komnata2divan():
    potratit_hod()
    print('под диваном лежит -', komnatapred[1][0])
    sleep(2)
    if komnatapred[1][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[1][0])
        komnatapred[1][0]='ничего'
    komnata2()

def komnata2shkaf():
    potratit_hod()
    print('в шкафу лежит -', komnatapred[1][1])
    sleep(2)
    if komnatapred[1][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[1][1])
        komnatapred[1][1]='ничего'
    komnata2()

def komnata2tumbochka():
    potratit_hod()
    print('в тумбочке лежит -', komnatapred[1][2])
    sleep(2)
    if komnatapred[1][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[1][2])
        komnatapred[1][2]='ничего'
    komnata2()

def komnata3shkaf():
    potratit_hod()
    print('в шкафу лежит -', komnatapred[2][0])
    sleep(2)
    if komnatapred[2][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[2][0])
        komnatapred[2][0]='ничего'
    komnata3()

def komnata3kover():
    potratit_hod()
    print('под ковром лежит -', komnatapred[2][1])
    sleep(2)
    if komnatapred[2][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[2][1])
        komnatapred[2][1]='ничего'
    komnata3()

def komnata3tumbochka():
    potratit_hod()
    print('в тумбочке лежит -', komnatapred[2][2])
    sleep(2)
    if komnatapred[2][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[2][2])
        komnatapred[2][2]='ничего'
    komnata3()

def komnata4divan():
    potratit_hod()
    print('под диваном лежит -', komnatapred[3][0])
    sleep(2)
    if komnatapred[3][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[3][0])
        komnatapred[3][0]='ничего'
    komnata4()

def komnata4shkaf():
    potratit_hod()
    print('в шкафу лежит -', komnatapred[3][1])
    sleep(2)
    if komnatapred[3][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[3][1])
        komnatapred[3][1]='ничего'
    komnata4()

def komnata4tumbochka():
    potratit_hod()
    print('в тумбочке лежит -', komnatapred[3][2])
    sleep(2)
    if komnatapred[3][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[3][2])
        komnatapred[3][2]='ничего'
    komnata4()

def komnata5tumbochka():
    potratit_hod()
    print('в тумбочке лежит -', komnatapred[4][0])
    sleep(2)
    if komnatapred[4][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[4][0])
        komnatapred[4][0]='ничего'
    komnata5()

def komnata5korobka():
    potratit_hod()
    print('в коробке с картошкой лежит -', komnatapred[4][1])
    sleep(2)
    if komnatapred[4][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[4][1])
        komnatapred[4][1]='ничего'
    komnata5()

def komnata5stol():
    potratit_hod()
    print('в столе лежит -', komnatapred[4][2])
    sleep(2)
    if komnatapred[4][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[4][2])
        komnatapred[4][2]='ничего'
    komnata5()

def komnata6shkaf():
    potratit_hod()
    print('в шкафу лежит -', komnatapred[5][0])
    sleep(2)
    if komnatapred[5][0]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[5][0])
        komnatapred[5][0]='ничего'
    komnata6()

def komnata6stol():
    potratit_hod()
    print('в столе лежит -', komnatapred[5][1])
    sleep(2)
    if komnatapred[5][1]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[5][1])
        komnatapred[5][1]='ничего'
    komnata6()

def komnata6krovat():
    potratit_hod()
    print('под подушкой лежит -', komnatapred[5][2])
    sleep(2)
    if komnatapred[5][2]=='ничего':
        print('здесь пусто')
        sleep(2)
    else:
        print('вы взяли себе это в инвентарь')
        sleep(2)
        inventar.append(komnatapred[5][2])
        komnatapred[5][2]='ничего'
    komnata6()

def komnata6seif():
    potratit_hod()
    kluck=input('Введите код для сейфа: ')
    if kluck=='68745':
        print('Код верный! Сейф открывается...')
        sleep(2)
        print('в сейфе лежит -', komnatapred[5][3])
        sleep(2)
        if komnatapred[5][3]=='ничего':
            print('здесь пусто')
            sleep(2)
        else:
            print('вы взяли себе это в инвентарь')
            sleep(2)
            inventar.append(komnatapred[5][3])
            komnatapred[5][3]='ничего'
        komnata6()
    else:
        print('неправильно!!!')
        sleep(3)
        komnata6()

inventar=[]
blue=0
yellow=0
red=0
keykr='красный ключ'
keysi='синий ключ'
keyjel='жёлтый ключ'
zapiska='записка:68745'
predmeti=['часы','молоток','карта','лопата',keykr,keysi,keyjel,zapiska]
komnatapred=[[],[],[],[],[],[]]

def spryatatpredmeti():
    global predmeti
    s=random.randint(1,10)
    if s<=5:
        if len(predmeti)==0:
            pass
            return None
        else:
            ss=random.choice(predmeti)
            predmeti.remove(ss)
            return ss
    else:
        return None

def vivodinventarya(a,b):
    vivod='ваш инвентарь:\n'
    if len(a)==0:
        vivod+='Пустой'
    else:
        for r in a:
            vivod+=r
            vivod+='\n'
    print(vivod)
    sleep(3)
    if b==komnata6 and 'молоток' in inventar:
        hod=input('ваши действия:\n1. выбить окно и выпрыгнуть\n2. нет\n')
        if hod=='1':
            print('вы ломаете окно и выпрыгиваете на улицу')
            sleep(3)
            koncovka()
            sys.exit()
        elif hod=='2':
            pass
        else:
            print('что-то не понятно, повторите пожалуйста')
            sleep(2)
            vivodinventarya(inventar,b)
    if b==komnata5 and 'лопата' in inventar:
        hod=input('ваши действия:\n1. выкопать проход на улицу\n2. нет\n')
        if hod=='1':
            print('вы выкапываетесь, но как вы понимаете вы не успели во время')
            sleep(3)
            badkoncovka()
            sys.exit()
        elif hod=='2':
            pass
        else:
            print('что-то не понятно, повторите пожалуйста')
            sleep(2)
            vivodinventarya(inventar,b)
    if 'карта' in inventar:
        hod=input('ваши действия:\n1. посмотреть карту\n2. нет\n')
        if hod=='1':
            print('''┌───────────┬───────────┬───────────┬───────────┬───────────┐
│           │           │           │           │           │
│  Комната  │  Комната  │  Комната  │  Комната  │  Комната  │
│     1     │     2     │     3     │     4     │     5     │
│           │           │           │           │           │
└───────────┴───────────┴─────┬─────┴───────────┴───────────┘
                              │
                              │
                              ▼
                        ┌───────────┐
                        │           │
                        │  ПОДВАЛ   │
                        │           │
                        └───────────┘''')
            sleep(4)
            pass
        elif hod=='2':
            pass
        else:
            print('что-то не понятно, повторите пожалуйста')
            sleep(2)
            vivodinventarya(inventar,b)
    if 'часы' in inventar:
        hod=input('ваши действия:\n1. посмотреть время\n2. нет\n')
        if hod=='1':
            print(hods//10,':',(hods-hods//10*10)*10)
            sleep(3)
            pass
        elif hod=='2':
            pass
        else:
            print('что-то не понятно, повторите пожалуйста')
            sleep(2)
            vivodinventarya(inventar,b)
    b()

for r in range(6):
    for t in range(3):
        d=spryatatpredmeti()
        if d==None:
            komnatapred[r].append('ничего')
        else:
            komnatapred[r].append(d)
komnatapred[5].append('актимелька из эльдорадо')

for r in komnatapred:
    if keysi in r:
        blue=1
if blue==0:
    while blue==0:
        g=random.randint(0,5)
        gg=random.randint(0,2)
        if komnatapred[g][gg]=='ничего':
            komnatapred[g][gg]=keysi
        for r in komnatapred:
            if keysi in r:
                blue=1

if keysi in komnatapred[4]:
    while keysi in komnatapred[4]:
        g=random.randint(0,3)
        gg=random.randint(0,2)
        if komnatapred[g][gg]=='ничего':
            for n in komnatapred:
                if keysi in n:
                    komnatapred[komnatapred.index(n)][n.index(keysi)]='ничего'
            komnatapred[g][gg]=keysi

for r in komnatapred:
    if keyjel in r:
        yellow=1
if yellow==0:
    while yellow==0:
        g=random.randint(0,5)
        gg=random.randint(0,2)
        if komnatapred[g][gg]=='ничего':
            komnatapred[g][gg]=keyjel
        for r in komnatapred:
            if keyjel in r:
                yellow=1
if keyjel in komnatapred[5]:
    while keyjel in komnatapred[5]:
        g=random.randint(0,4)
        gg=random.randint(0,2)
        if komnatapred[g][gg]=='ничего':
            for n in komnatapred:
                if keyjel in n:
                    komnatapred[komnatapred.index(n)][n.index(keyjel)]='ничего'
            komnatapred[g][gg]=keyjel

for r in komnatapred:
    if keykr in r:
        red=1
if red==0:
    while red==0:
        g=random.randint(0,5)
        gg=random.randint(0,2)
        if komnatapred[g][gg]=='ничего':
            komnatapred[g][gg]=keykr
        for r in komnatapred:
            if keykr in r:
                red=1

name=input('введите ваше реальное имя!!!!')
print('Темно, вы просыпаетесь на какой-то кровати и ничего не помните')
sleep(3)
print('и вдруг вы вспоминаете что сейчас вы проходите квест')
sleep(3)
print('Условия квеста: если успеете выбраться из таинственного дома за 5 часов, то получите приз!')
sleep(3)
print('вы встаёте')
sleep(2)
komnata1()
