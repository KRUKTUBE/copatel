# массив поля, * — пустое поле, # — стена
import random
pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","#","#","#","#","#"],
        ["*","*","*","#","#","#","#","#","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]

# то, что будет выводиться на экран
vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]

# вывод поля на экран, для любого, абстрактного списка будет работать


def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()

x = random.randint(0, 11)
y = random.randint(0, 11)
e = random.randint(0, 11)
r = random.randint(0, 11)
g = random.randint(0, 11)
h = random.randint(0, 11)
v = random.randint(0, 11)
b = random.randint(0, 11)
pole[x][y] = "0"
pole[e][r] = "0"
pole[v][b] = "0"


# проверка поля на то, что внутри него
# если поле пустое, проверяются все клетки вокруг него
# если стена — не проверяются
# если поле уже было открыто — оно не проверяется

def check(stroka,stolb):
    # если клетка ещё не открыта
    if vidimost_polya[stroka][stolb] == "•":
        # открываем
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        
        # если оно оказалось пустым
        if pole[stroka][stolb] == "*":
            # проверяем все соседние, только если они существуют
            # а то выйдем за пределы поля, Python ругать будет
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
                
                

                for i in range(0, 11):
                    if pole[stroka+i][stolb] == "0":
                        pole[stroka+i+1][stolb]= "1"
                        pole[stroka+i-1][stolb]="1"
                        pole[stroka+i][stolb + 1]="1"
                        pole[stroka+i][stolb - 1]="1"    
# добавим проверку, остались ли ещё неоткрытые элементы поля
# функция будет возвращать True, если больше нет
# и False, если ещё остались

def isOpen():
    # считаем, что поле открыто всё
    opened = True
    #для каждой строки в видимости поля
    for stroka in vidimost_polya:
        # если хотя бы в одной нашлось закрытое поле
        if "•" in stroka:
            # значит неправда, поле ещё не всё открыто
            opened = False
    return opened