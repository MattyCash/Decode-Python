#7CL

#A
# for i in range(5,16):
#     if i == 10:
#         continue
#     print(i)

#B
# a = int(input())
# for i in range(0,a+1):
#     print(i)

#C
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i)

#D
# a = int(input())
# b = int(input())
# for i in range(a, b-1, -1):
#     if i % 2 != 0:
#         print(i)

#A
# a = str(input())
# for i in a:
#     print(i, end =' ')

#B
# a = int(input())
# b = int(input())
# sum = 0
# for i in range(a, b + 1):
#     sum = sum + i
# print(sum)

#C
# a = int(input())
# b = int(input())
# x = 0
# for i in range(1, (a*b)):
#     if(a % i == 0 and b % i == 0):
#         x = i
# print(a * b / x)

#A
# a = int(input())
# cnt = 0
# for i in range(1,a+1):
#     if(a % i == 0):
#         cnt+=1
# if(cnt == 2):
#     print("Prime")
# elif(cnt > 2):
#     print("Common")
# else:
#     print("Common")



#B
# n = int(input())
# s = 0
# for i in range(n):
#     x = input()
#     if 'a' <= x <= 'z':
#         s += ord(x)-96
#     elif 'A' <= x <= 'Z':
#         s += ord(x)-64

# print(s)

#C
# a = int(input())
# b = int(input())
# x = int(input())
# for i in range(a,b+1):
#     j = i
#     s = 0
#     while j > 0:
#         s += j % 10
#         x //= 10
#     if s == x:
#         print(i, end = ' ')


#7HW

#A
# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b + 1):
#         print(i, end=' ')
# else:
#     for i in range(a, b - 1, -1):
#         print(i, end=' ')

#B
# a = int(input())
# b = int(input())
# for i in range(a-1, b - 1, -2):
#         print(i, end=' ')

#A
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(a, b+1):
#     if(i % d == c):
#         print(i, end=' ')

#B
# n = int(input())
# s = 0
# for i in range(n):
#     x = int(input())
#     s += x
  
# print(s)


#A
## i = s - j  
## (s-j)*j = m

# s = int(input())
# m = int(input())
# for i in range(1,1001):
#     j = s - i
#     if(i <= j and i * j == m):
#         print(i,j, end=' ')
#         break

#B
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(-100,101):
#     if a*(i**3) + b*(i**2) + c * i + d == 0:
#         print(i, end=' ')
        