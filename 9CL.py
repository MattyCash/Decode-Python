#A
# a = []
# for i in range(3):
#     new_element = str(input())
#     a.append(new_element)
# print(a)

#B
# a = list(map(int,input().split()))
# print(a)

#C
# a = list(map(int,input().split()))
# i = 0
# for i in range(len(a)):
#     if len(a) > 1:
#        print(a[0], a[len(a)-1])
#        break
#     else:
#         print(*a)


#D
# a = list(map(int,input().split()))
# print(sum(a))

#A
# a = list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i] > 0:
#       print(a[i], end=' ')

#B
# a = list(map(int,input().split()))
# a.sort(reverse=True)
# print(*a)

#C
# a = list(map(int,input().split()))
# print(max(a))

#A
# a = list(map(int,input().split()))
# n = int(input())
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] + a[j] == n:
#           print(a[i],a[j])

#B
# a = list(map(int,input().split()))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(*b)

#C
# a = input().split()
# a.sort()
# a.sort(key = len)
# print(a)

#A easy
# a = []
# n = int(input())
# for i in range(n):
#     new_element = input()
#     a.append(new_element)
# print(a)

#B easy
# array = []
# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a % 2 != 0:
#         array.append(a)
# print(*array)

#A medium
# array = []
# n = int(input())
# mx = -10000
# cnt = -1
# for i in range(n):
#     a = int(input())
#     if a > mx:
#         mx = a
#         cnt += 1
# print(mx, cnt)

#B medium
# a = list(map(int,input().split()))
# k=int(input())
# print(a.count(k))

#A hard  
# a = list(map(int,input().split()))
# # a[0],a[4] = a[4],a[0]
# a[a.index(max(a))],a[a.index(min(a))] = a[a.index(min(a))],a[a.index(max(a))]
# print(*a)      

#B hard
# a = list(map(int,input().split()))
# cnt = 0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i] == a[j]):
#             cnt+=1
# print(cnt)          