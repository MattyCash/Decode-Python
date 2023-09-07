#6CL

from random import randint

#A
# x = randint(1,100)
# cnt = 0
# print("Угадай число!","Случайное число находиться между 1 и 100 ", " У вас есть неогранниченное количество попыток", " Игра начинается...", sep="\n")
# while True:
#    cnt = cnt + 1
#    print("Попытка #", cnt, " Введите число:", sep=' ')
#    b = int(input())
#    if(b != x): 
#        print("Вы не угадали!", sep=' ')
#        continue
#    else:
#        print("Поздравляем! Вы угадали число.", "У вас ушло", cnt, "попыток", sep=' ')
#        break
    
#B
# b = randint(1,3)
# x = 0
# cnt1 = 0
# cnt2 = 0
# print("Камень-ножницы-бумага!",'Вы будете играть с компьютером в "су-ли-фа"', "Компьютер уже сделал свой выбор!","Теперь ваша очередь...", sep='\n')
# print("1--Камень","2--Ножницы","3--Бумага", sep='\n')
# while True:
#    print("Сделайте свой выбор:")
#    a = int(input())
#    if(cnt1 == 3 and cnt2 < 3):
#         print("Тотальная доминцаия человека!","Человек:", cnt1, "Компьютер:", cnt2, sep = ' ')
#         exit()
#    elif(cnt1 < 3 and cnt2 == 3):
#         print("Тотальная доминцаия компьютера!","Человек: ", cnt1, "Компьютер:", cnt2, sep = ' ')
#         exit()
#    if(a == b):
#        if(a == 1 and b == 1):
#            print("Выбор компьютера: Камень", "Ваш выбор: Камень", "Ничья", sep='\n')
#            continue
#        elif(a == 2 and b == 2):
#            print("Выбор компьютера: Ножницы", "Ваш выбор: Ножницы", "Ничья", sep='\n')
#            continue
#        elif(a == 3 and b == 3):
#            print("Выбор компьютера: Бумага", "Ваш выбор: Бумага", "Ничья", sep='\n')
#            continue
    
#    elif((a != b) and ((a == 3) and (b == 1))):
#        print("Выбор компьютера: Камень", "Ваш выбор: Бумага", "Вы победили компьютер!", sep='\n')
#        cnt1 += 1
#        continue
#    elif((a != b) and ((a == 2) and (b == 3))):
#        print("Выбор компьютера: Бумага", "Ваш выбор: Ножницы", "Вы победили компьютер!", sep='\n')
#        cnt1 += 1
#        continue
#    elif((a != b) and ((a == 1) and (b == 2))):
#        print("Выбор компьютера: Ножницы", "Ваш выбор: Камень", "Вы победили компьютер!", sep='\n')
#        cnt1 += 1
#        continue

#    elif((a != b) and ((a == 3) and (b == 2))):
#        print("Выбор компьютера: Ножницы", "Ваш выбор: Бумага", "Вы проиграли!", sep='\n')
#        cnt2 += 1
#        continue
#    elif((a != b) and ((a == 2) and (b == 1))):
#        print("Выбор компьютера: Камень", "Ваш выбор: Ножницы", "Вы проиграли!", sep='\n')
#        cnt2 += 1
#        continue
#    elif((a != b) and ((a == 1) and (b == 3))):
#        print("Выбор компьютера: Бумага", "Ваш выбор: Камень", "Вы проиграли!", sep='\n')
#        cnt2 += 1
#        continue

#    elif(a > 3 or a < 0):
#        print("Неверный выбор! Повторите попытку")
#        continue


#C
# b = randint(1,2)
# x = randint(1,2)
# print("Шарик с предсказаниями!","Каждый раз шарик будет выдавать случайное предсказание.", "А так же можете задать свой вопрос и получить ответ.", sep=' ')
# while True: 
#     print("Выберите режим:")
#     print("Режимы:", "1)Предсказания.", "2)Задать вопрос.", sep = '\n')
#     a = int(input())
#     if(a == 1):
#         print("У вас будет неудачный день!")
#         print("Продолжаем(Да/Нет)?")
#         c = str(input())
#         if(c == 'Да'):
#             continue
#         elif(c == 'Нет'):
#             print("GoodBye!")
#             break
        
#     elif(a == 2):
#         print("Задайте свой вопрос:")
#         a = str(input())
#         print("1 = Да, 2 = Нет")
#         print("Ответ на мой вопрос:", b)
#         print("Продолжаем(Да/Нет)?")
#         c = int(input())
#         if(c == 'Да'):
#           continue
#         elif(c == 'Нет'):
#             print("GoodBye!")
#             break


#D
# print("Консольный калькуятор","Здесь вы сможете делать простые математические вычисления!", sep='\n')
# while True:
#   print("Введите первое число: ")
#   a = float(input())
#   print("(+, -, /, **, //, %)", "Введите операцию: ", sep='\n')
#   op = str(input())
#   print("Введите второе число: ")
#   b = float(input())

#   if(op == '+'):
#     print("Результат", a + b)
#     print("Продолжаем(Да/Нет)?")
#     c = str(input())
#     if(c == 'Да'):
#         continue
#     elif(c == 'Нет'):
#         break
#     print("Goodbye!")
#   elif(op == '-'):
#     print("Результат", a - b)
#     print("Продолжаем(Да/Нет)?")
#     c = str(input())
#     if(c == 'Да'):
#         continue
#     elif(c == 'Нет'):
#         break
#     print("Goodbye!")
#   elif(op == '**'):
#     print("Результат", a ** b)
#     print("Продолжаем(Да/Нет)?")
#     c = str(input())
#     if(c == 'Да'):
#         continue
#     elif(c == 'Нет'):
#         break
#     print("Goodbye!")
#   elif(op == '//'):
#     print("Результат", a // b)
#     print("Продолжаем(Да/Нет)?")
#     c = str(input())
#     if(c == 'Да'):
#         continue
#     elif(c == 'Нет'):
#         break
#     print("Goodbye!")
#   elif(op == '%'):
#     print("Результат", a % b)
#     print("Продолжаем(Да/Нет)?")
#     c = str(input())
#     if(c == 'Да'):
#         continue
#     elif(c == 'Нет'):
#         break
#     print("Goodbye!")
#   else:
#     print("Неверная операция!")


