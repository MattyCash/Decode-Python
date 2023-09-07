#try except
#A easy
# a = int(input())
# if a < 0:
#     raise ValueError("Ошибка ввода!")

#B Easy
# def integer(s):
#     try:
#       int(s)
#       return True
#     except ValueError:
#       return "srsly?"

# s = input()
# print(integer(s))

#C Easy
# n = str(input())
# if n.istitle():
#     print("welcome")
# else:
#     raise NameError("Cheu ty...")

#A Medium
# n = str(input())
# if n.isalpha():
#     print("welcome")
# else:
#     raise NameError("Cheu ty...")

#B Medium
# n = str(input())
# if n.find('@') > 1:
#     print("welcome")
# else:
#     raise NameError("Cheu ty...")

#C Medium
# n=input()

# for i in n:
#     if i=="@":
#         break
#     if  not i.islower():
#         raise ValueError("чел ты")
# print("welcome")

#HW try execpt
#A Easy
# d= eval(input())
# k = input()
# try :
#     print(d[k])
# except KeyError:
#     print("That key does not exist!")

#B Easy
# def check(a,b):
#     return b if a > b else a

# a = int(input())
# b = int(input())
# print(check(a,b))

#A Medium 
# a=eval(input())
# for i in a:
#     if i % 3 == 0 and i %5 ==0:
#         print('Такое число присутствует')
#         exit()
# raise ValueError("Такое число отсутствует")

#B Medium 
# def summa(a,b,c):
#       if a * b == c:
#             return True
#       else:
#             raise Exception(False)

# a = int(input())
# b = int(input())
# c = int(input())
# print(summa(a,b,c))

#A Hard 
# def op(num1, num2, operator):
#     try:
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         else:
#             raise ValueError("Invalid operator")
#     except Exception as e:
#         print(e)

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")
# print(op(num1, num2, operator))

#B Hard
# def check(a):
#  first = a // 1000
#  second = a % 1000 // 100
#  third = a % 1000 % 100 // 10
#  last = a % 1000 % 100 % 10
#  return True if first % 3 == 0 or second % 3 == 0 or third % 3 == 0 or last % 3 == 0 else False

# a = int(input())
# print(check(a))