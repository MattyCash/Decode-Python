#functions 
#A Easy
# def check(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# a = int(input())
# check(a)

#B Easy
# def alpha(str):
#     print(min(str))

# str = list(map(str,input().split()))
# alpha(str)


#C Easy
# def is_power_two(x):
#     i = 0
#     if x % 2 == 0:
#         while 2 ** i < x:
#             i += 1
#         else:
#             print("YES")
#     else:
#         print("NO")

# x = int(input())
# print(is_power_two(x))

#D Easy
# def findn(n,x):
#     for i in range(len(n)):
#         if n[i] == x:
#             print(i) 
#             break
#         else:
#             continue

# n = list(map(int,input().split()))
# x = int(input())
# findn(n,x)

#E Easy
# def have_digit(s):
#     for i in s:
#         if i.isdigit():
#             return "cool"
#     return "hot"


# s = input()

# print(have_digit(s)

#A Medium
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

#B Medium
# def str_sort(str):
#    print(*sorted(str))

# str = str(input())
# str_sort(str)

#C Medium
# def unique(n):
#     arr = []
#     for i in n:
#         if i not in arr:
#             arr.append(i)

#     n = arr
#     print(*n)

# n = list(map(int,input().split()))
# unique(n)

#D Medium
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

#E Medium
# def sub(arr):
#     s = []
#     for x in arr:
#         s.append((x + 5) // 5)
#     return max(s)


# arr = list(map(int,input().split()))
# print(sub(arr))

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
# def top(movies):
#     high_rated = []
#     for movie in movies:
#         name, rating = movie.split(" ")
#         if float(rating) >= 7:
#             high_rated.append(name)
#     return high_rated

# n = int(input())
# movies = []
# for i in range(n):
#     movies.append(input())
# print(*top(movies))

#C Hard
# def existing_letters(s):
#     s = s.lower()
#     existing_letters = set()
#     for i in s:
#         if i.isalpha():
#             existing_letters.add(i)
 
#     return existing_letters

# s = str(input())
# print(*existing_letters(s))


#E Hard
# def k_max(a,k):
#     a=list(set(a))
#     a.sort()
#     a.reverse()
#     return a[k-1]

# a= list(map(int,input().split()))
# k=int(input())
# print(k_max(a,k))
