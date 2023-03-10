import mylib
# массивы и функция vyvodPolya в файле mylib.py           

        
mylib.vyvodPolya(mylib.vidimost_polya)
game = True
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    # передадим не номера строки и столбца, а индексы
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.vidimost_polya[stroka][stolb] == "0":
        print("поражение мозга")
        game = False
    if mylib.isOpen():
        game = False
        
    

1
