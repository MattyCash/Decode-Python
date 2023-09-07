#Strings

#10CL
#A easy
# a = list(map(str,input().split()))
# print(*a, sep="\n")

#B easy
# a = list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i] > 0:
#       print(a[i], end=' ')

#C easy
# a = list(map(int,input().split()))
# cnt = 0
# for i in range(len(a)):
#     if a[i] == 0:
#         cnt += 1
# print(cnt, end=' ')

#D easy 
# a = list(map(int,input().split()))
# sum = 0
# for i in range(len(a)):
#     sum += a[i]
# if(sum > 10):
#     print("More")
# elif(sum < 10):
#     print("Less")
# elif(sum == 10):
#     print("Equal")

#E easy
# a = list(map(int,input().split()))
# a.sort(reverse=True)
# print(*a)

#A medium 
# a = list(map(int,input().split()))
# n = int(input())
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] + a[j] == n:
#           print(a[i],a[j])

#B medium
# a = list(map(int,input().split()))
# print(a.index(max(a)))

#C medium
# a = list(map(int,input().split()))
# print(max(a)-min(a))

#D medium
# a = list(map(int,input().split()))
# arr = []
# i = 0


#E medium
# a = list(map(int,input().split()))
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(*b)

#A hard 

#B hard
# s = input().split()
# let = input()
# first= None
# second = None
# i=0
# j=len(s)-1

# while first == None or second == None:
#     if s[i] == let:
#         first = i
#     else:
#         i+=1
    
#     if let == s[j]:
#         second = j
#     else:
#         j-=1

# if i == j:
#     print(i)
# else:
#     print(i,j)
            
#C hard
# a = list(map(int,input().split()))
# a.sort()
# print(*a)


#D hard
# words = input().split()
# words.sort()

# l = [len(word) for word in words]

# for _ in range(len(l)):
#     max_len = max(l)

#     print(words[l.index(max_len)], end=' ')
    
#     words.pop(l.index(max_len))
#     l.remove(max_len)



#E hard
