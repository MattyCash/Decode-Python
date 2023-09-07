#18CL 
# Easy A
# var = [13, 4, 7, 5, 6, 9]

#Easy B
# Student = {
#     'name' : 'Aidana',
#     'age' : 21,
#     'gpa' : 3.88
# }

#Medium A
# def rev(string):
#     return string[::-1]

#Hard A
# def summa(numbers):
#     # mn = numbers.index(min(numbers))
#     # mx = numbers.index(max(numbers))
#     mn = min(numbers)
#     mx = max(numbers)
#     return mn + mx

#Hard B
# def freq(string):
#     cnt = {}
#     for letter in string:
#         if letter in cnt:
#             cnt[letter] += 1
#         else:
#             cnt[letter] = 1
#     return cnt

#HW 18
#Medium A
# def summa(a):
#  first = a // 1000
#  second = a % 1000 // 100
#  third = a % 1000 % 100 // 10
#  last = a % 1000 % 100 % 10
#  return first + second + third + last

#Medium B
# import math

# def abs_val(x):
#     return abs(x)

# def square_root(x):
#     return math.sqrt(x)

# def factorial(x):
#     return math.factorial(x)



# n = int(input())
# chars = list(map(int, input().split()))
# rows = list(map(int, input().split()))
# keyboard = {}
# for i in range(n):
#     keyboard[chars[i]] = rows[i]

# k = int(input())
# text = list(map(int, input().split()))

# count = 0
# for i in range(1, k):
#     if keyboard[text[i]] != keyboard[text[i-1]]:
#         count += 1

# print(count)



# n, m, q = map(int, input().split())

# servers = [[1] * m for i in range(n)]
# restarts = [0] * n

# def prod(i):
#     return restarts[i] * sum(servers[i])

# max_prod_i = min_prod_i = 0
# results = []

# for i in range(q):
#     query = input().split()
#     if query[0] == "RESET":
#         restarts[int(query[1])-1] += 1

#     elif query[0] == "DISABLE":
#          i, j = map(int, query[1:])
#          servers[i-1][j-1] = 0

#     elif query[0] == "GETMAX":
#         max_prod_i = max(range(n), key=prod) + 1
#         results.append(max_prod_i)

#     elif query[0] == "GETMIN":
#          min_prod_i = min(range(n), key=prod) + 1
#          results.append(min_prod_i)
         
    
# print(*results, sep='\n')



# Коля и дата-центры
# n, m, q = map(int, input().split())

# R = [0] * n
# A = [m] * n

# max_center = 1
# min_center = 1

# max_prod = R[0] * A[0]
# min_prod = R[0] * A[0]
# answers = []

# for i in range(q):
#     query = input().split()

#     if query[0] == 'RESET':
#         center = int(query[1]) - 1
#         R[center] += 1

#     elif query[0] == 'DISABLE':
#         center, server = map(int, query[1:])
#         center -= 1
#         server -= 1
#         A[center] -= 1

#     elif query[0] == 'GETMAX':
#         # находим дата-центр с максимальным произведением R[i]*A[i]
#         max_prod = R[0] * A[0]
#         max_center = 1
#         for j in range(1, n):
#             prod = R[j] * A[j]
#             if prod > max_prod:
#                 max_prod = prod
#                 max_center = j + 1
#         answers.append(max_center)

#     elif query[0] == 'GETMIN':
#         # находим дата-центр с минимальным произведением R[i]*A[i]
#         min_prod = R[0] * A[0]
#         min_center = 1
#         for j in range(1, n):
#             prod = R[j] * A[j]
#             if prod < min_prod:
#                 min_prod = prod
#                 min_center = j + 1
#         answers.append(min_center)

# for ans in answers:
#     print(ans)
