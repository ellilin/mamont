f = open("input.csv", "r")
f1 = open("output_5.2.txt", "w")

sumali = 0      #ценность всех грузов для Алисы
sumcha = 0      #ценность всех грузов для Чарли

for i in f:

    s=i.split(';')
    sumali+=int(s[2])
    sumcha+=int(s[4])
f.close()
f = open("input.csv", "r")

for i in f:
    s=i.split(';')
    f1.write(s[0] + ';' + s[1] + ';' + str(round(((int(s[2])/sumali)*100), 3)) + ';' + str(round(((int(s[4])/sumcha)*100),3))  + '\n')

f1.close()
f.close()

f = open("output_5.2.txt", "r")

sumali = 0      #ценность грузов для Алисы
sumcha = 0      #ценность грузов для Чарли
kali = 0        #количество грузов Алисы
kcha = 0        #количество грузов Чарли


for i in f:

    s=i.split(';')
    print(s[0], '   ',s[1], end = ' ')      #Выводим номер груза и его название

    if float(sumali) <  float(sumcha):      #Сравниваем ценности Алисы и Чарли, если суммарная меньше у Алисы, отдаём ей груз
        print('Алиса')                      #Отдаём груз Алисе
        sumali+=float(s[2])                 #Добавляем в итоговую сумму ценностей Алисы, ценность данного груза
        kali+=1                             #Добавляем единичку к количеству имеющихся у Алисы предметов

    elif float(sumali) >=  float(sumcha):   #Если суммарная ценность у Чарли больше суммарной ценности Алисы
        print('Чарли')                      #Отдаём груз Чарли
        sumcha+=float(s[3])                 #Добавляем в итоговую сумму ценностей Чарли ценность данного груза
        kcha+=1                             #Добавляем единичку к количеству имеющихся у Чарли предметов

print("Алиса ценность:", sumali, " количество:", kali)
print("Чарли ценность:", sumcha, " количество:", kcha)

f.close()