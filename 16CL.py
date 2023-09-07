#A Easy 
# def recursion():
#     print("This is recursion")
#     recursion()

# recursion()

#B Easy
# def f(n):
#     if n > 0:
#         f(n-1)
#         print(n,end=" ")

# f(int(input()))

#C Easy
# def f(n):
#     if n == 1:
#         return 1
#     return n*f(n-1)    

# n=int(input())

# print(f(n))

#D Easy
# def A(m, n):
#     if m == 0:
#         return n + 1
#     elif n == 0:
#         return A(m-1, 1)
#     else:
#         return A(m-1, A(m, n-1))


#A Medium
# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + summa(n // 10)

# n = int(input())
# print(summa(n))

#B Medium
# def f(a):
#     if len(a)==0:
#         return 0
#     return f(a[:-1])+a[-1]

# a=list(map(int,input().split()))
# print(f(a))

#C Medium
# def fun(n):
#     if n == 1:
#         return True
#     elif n % 2 == 0:
#         return fun(n//2)
#     else:
#         return False

# n = int(input())
# print(fun(n))

#A Hard
# def f(n,k=2):
#     if n ==1:
#         return
#     if n % k ==0:
#         print(k,end= " ")
#         return f(n/k)
#     return f(n,k+1)

# f(int(input()))

#B Hard
# def b(n):
#     if n==0:
#         return 
#     b(n//2)
#     print(n%2 ,end="")


# n=int(input())

# b(n)

#C Hard
# def rev(n,s=0):
#     if n ==0:
#         return s
#     return rev(n//10,s*10+(n%10))

# n = int(input())

# print(rev(n))



#16HW

#A Easy
# def rev(n,s=0):
#     if n ==0:
#         return s
#     return rev(n//10,s*10+(n%10))

# n = int(input())

# print(rev(n))

#A Medium
# def Power(x, y):
#     if y == 1:
#         return x
#     else:
#         return x * Power(x, y-1)

# x = int(input())
# y = int(input())
# print(Power(x,y))

#A Hard
# def rec(n,k=1):
#     if n==0:
#         return
#     i=0
#     while i<k:
#         print(k,end=" ")
#         i+=1
#         n-=1
        
#         if n==0:
#             return
#     rec(n,k+1)

# n=int(input())

# rec(n)