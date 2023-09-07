#Sets

#A Easy
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1 | set2)
 
#B Easy
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1 & set2)

#C Easy
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1 - set2)
# print(set2 - set1)

#D Easy
# a = set(map(str,input().split()))
# print(a)

#A Medium
# s = set(input())
# print(len(s))
# print(*sorted(set(s)))

#B Medium
# n = int(input())
# s = set(input().split())
# print(n - len(s))

#C Medium
# s = set(input())
# s.discard(' ')
# s = sorted(s)
# print(*s)

#A Hard
# s = set(input())
# s= sorted(s , reverse= True)
# for i in s:
#     if i.isalpha():
#         print(i,end =" ")

#B Hard
# s1 = set()
# s2 = set()
# n = int(input())

# for i in range(n):
#     x=input()
#     s1.add(x)

# m = int(input())
# for i in range(m):
#     x=input()
#     s2.add(x)

# print('ABSENCE:')
# s3 = s2 - s1
# for i in sorted(s3):
#     print(i)
# print()
# print("IMPOSTER:")
# s4 = s1 - s2
# for i in sorted(s4):
#     print(i)

#C Hard
# a = input().split()
# s1 = set()
# s2 = set()

# for i in set(a):
#     if a.count(i) > 1:
#         s2.add(i)
#     else:
#         s1.add(i)

# print(s1)
# print(s2)


#Sets

#A Easy
# s = set(input().split())
# s1 = set()

# for i in s:
#     if int(i) % 3 != 0:
#         s1.add(int(i))

# print(*sorted(s1))

#B Easy
# s = set(map(int,input().split()))

# for i in sorted(s):
#     k = 1
#     while k <= i:
#         if k == i:
#             print(i, end=" ")
#             break
#         k *= 2

#A Medium
# s = set(input().split())
# print(max(s))
# print(min(s))

#B Medium
# s = set(map(int,input().split()))
# print(len(s))

#A Hard
# a = input().split()

# b = []

# for i in a:
#     if i in b:
#         print("YES")
#     else:
#         b.append(i)
#         print("NO")

#B Hard
# s = set(input().split())
# print(len(s))
