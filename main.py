#18CL 
# Easy A
# from module import var
#  print(var[0])

#Easy B
# from module import Student
# print(Student['name'], Student['age'])

#Easy C
#from random import randint
# a = int(input())
# b = int(input())
# print(randint(a,b))

#Medium A
# import module
# string = input()
# rev = module.rev(string) 
# print(rev)

#Medium B
# from math import sqrt, degrees,sin
# x = int(input())
# y = int(input())
# print((sqrt(sin(x) + pow(y,3)) + sqrt(x+y))/(2*x+y))

#Medium C
# from math import sin,cos,pow,exp
# print((sin(5) + pow(1.75,2)) / (3*exp(cos(7))))

#Hard A
# from module import summa
# numbers = list(map(int,input().split()))
# print(summa(numbers))

#Hard B
# from module import freq
# string = str(input())
# print(freq(string))
#HW 18
from math import sqrt,pow,tan,pi
from random import randint
#Easy A
# a = int(input())
# b = int(input())
# print(pow(sqrt(a) - sqrt(b),2))

#Easy B
# a = int(input())
# b = int(input())
# print(-tan((a*pi/b)))

#Medium A
# from module import summa
# a = randint(1000,9999)
# print(a, summa(a))

#Medium B
# from module import abs_val,square_root,factorial
# x = int(input())
# print("The absolute value of", x, "is", abs_val(x))
# print("The square root of", x, "is", square_root(x))
# print("The factorial of", x, "is", factorial(x))

#Hard A
# import random
# def finder(numbers):
#     mx = max(numbers)
#     cnt = 0
#     while True:
#         random_number = random.choice(numbers)
#         cnt += 1
#         if random_number == mx:
#             return cnt

# numbers = list(map(int,input().split()))
# print(finder(number)