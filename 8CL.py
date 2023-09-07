#A
# for i in range(1,100):
#     print(i, "----", 100-i, sep="")

#B
# n =int(input())
# f=1
# for i in range(2,n+1):
#   f*=i
# print(f)

#C
# n = int(input())
# for i in range(1,n+1):
#     print(i*"*")

#D
# n = int(input())
# cnt = 0
# for  i in range(n):
#     x = int(input())
#     if x % 10 == 8:
#         cnt+=1
# print(cnt)


#A
# n = int(input())
# k=int(input())
# for  i in range(k,(n*k)+1,k):
#     print(i,end=" ")

#C
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,sep="")

#A
# n = int(input())
# cnt =0
# for i in range(n):
#     x =input()
#     for j in x:
#         if j == '0':
#             cnt +=1
# print(cnt)

#B
# a =int(input())
# b=int(input())

# for i in range(a,b+1):
#     flag = True
#     for j in range(2,i):
#         if i % j ==0:
#             flag = False
#             break
#     if flag and i !=1:
#         print(i,end=" ")


#C
# n = int(input())

# first = 0
# second = 1

# for i in range(n-1):
#     first,second =second , first+second
# print(first)

#A
# import math
# a = int(input())
# b = int(input())

# for i in range (a,b+1):
#     if(math.sqrt(i * 1.0) == int(math.sqrt(i))):
#         print(i, end=" ")


#B
# a = int(input())
# for i in range(1,a+1):
#     if(a % i == 0):
#         print(i, end=" ")


#A
# n = int(input())
# for i in range(n):
#     x = int(input())
#     if(x == 0):
#         print("YES")
#     else:
#         print("NO")

#B
# n = int(input())
# zer = 0
# pos = 0
# neg = 0
# for i in range (n):
#     a = int(input())
#     if(a == 0):
#         zer+=1
#     elif(a > 0):
#         pos+=1
#     elif(a < 0):
#         neg+=1
# print(zer, pos, neg, sep='\n')


#A
# a = int(input())
# for i in range(a):
#     for j in range(1, i+2):
#         print(j, end='')
#     print()


#B
