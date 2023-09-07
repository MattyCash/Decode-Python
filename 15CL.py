#functions 
#A Easy
# def print_text():
#     print("Hi there,I am using WhatsApp")

# print_text()

#B Easy 
# def print_text(a):
#     print("I am " + a + " years old.")

# a = input()
# print_text(a)

#C Easy
# def check(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# a = int(input())
# check(a)

#D Easy
# def summa(n):
#     s = 0
#     for i in range(1,n+1):
#         s+=i
#     return s

# n = int(input())
# print(summa(n))

#A Medium
# def have_digit(s):
#     for i in s:
#         if i.isdigit():
#             return "cool"
#     return "hot"


# s = input()

# print(have_digit(s)

#B Medium
# def is_prime(a):
#     cnt = 0
#     i = 1
#     for i in range(2,a):
#         if a % i == 0:
#             cnt += 1
    
#     if cnt > 1:
#         print("False")
#     else:
#         print("True")

# a = int(input())
# is_prime(a) 

#C Medium
# def sum_of_digits(n):
#     s = 0
#     while n>0:
#         s+=n%10
#         n//=10
#     return s

# n = int(input())

# print(sum_of_digits(n))

#A Hard
# def sort(a):
#     b= []
#     c=[]
#     for i in a:
#         if i % 2==0:
#             b.append(i)
#         else:
#             c.append(i)
#     b.sort()
#     c.sort()
#     return b+c


# a= list(map(int,input().split()))



# print(*sort(a))

#B Hard
# def k_max(a,k):
#     a=list(set(a))
#     a.sort()
#     a.reverse()
#     return a[k-1]

# a= list(map(int,input().split()))
# k=int(input())
# print(k_max(a,k))

#C Hard
# def onlydigit(s):
#     cnt = 0
#     for i in s:
#         if i.isdigit():
#             cnt+=1
#     if cnt == len(s):
#         return "very good"
#     elif cnt >0:
#         return "not bad"
#     return "so bad"

# s= input()

# print(onlydigit(s))



#functions HW
#A Easy
# def power(a,n):
#     print(a**n)

# a = float(input())
# n = float(input())
# power(a,n)

#B Easy
# def is_year_leap(a):
#     if((a % 4 == 0 and a % 100 != 0) or (a %400 == 0)):
#         return True
#     return False

# a = int(input())
# print(is_year_leap(a))

#A Medium
# def get_nod(a,b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a  

#     return a

# a = int(input())    
# b = int(input())    
# print(get_nod(a,b))      

#B Medium 
# def avg(a):
#     s = 0
#     for i in range(len(a)):
#         s += a[i]
#     return (s/len(a))

# a = list(map(int,input().split()))
# print(avg(a))

#A Hard 
# def summa(n):
#     s = 0
#     while len(n) > 0:
#         s += n % 10
#         n = n // 10
#     return s


# n = list(map(int,input().split()))
# print(summa(n))

    
