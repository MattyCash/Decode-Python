#5CL

#A
# i = 0
# a = int(input())
# while i < a:
#     print("DeCode") 
#     i += 1


#B
# a = int(input())
# i = 0
# cnt = 0
# while i < a:
#     i += 1
#     cnt = cnt + i
#     if(i == a):
#         print(cnt)  

#C
# a =int(input())
# b =int(input())

# while a<=b:
#     if a % 2 ==0:
#         print(a ,end = " ")
#     a+=1



#A
# a = int(input())
# i = 1
# while i <= a:
#     i *= 2
#     if(i == a):
#         print("yes")
#         break
#     elif(a == 1):
#         print("yes")
#         break


# if(i != a and a != 1):
#     print("no")


#B
# a = int(input())
# cnt = 0
# while a > 0:
#     b = a % 10
#     cnt = cnt + b
#     a = a // 10
# print(cnt)

#C
# a = float(input())
# cnt = 0
# while a >= 1:
#         a = a / 2
#         cnt += 1
        
# print(cnt)


#A
# a = int(input())
# b = int(input())
# cnt = 0
# while a < b:
#     a = a * 3
#     b = b * 2
#     cnt = cnt + 1

# print(cnt)


#B
# s = 0
# s2=0

# while True:
#     x= int(input())
#     s+=x
#     s2+=x*x
#     if s == 0:
#         print(s2)
#         break


#vzyal u vas 


#C
# n = int(input())
# sum = 0
# i = 0
# while i < n:
#     x = int(input())
#     sum += x
#     i += 1

# print(sum)


#5HW


#A
# a = int(input())
# min = 0
# i = 1
# while i <= a:
#     i += 1
#     if(a % i == 0):
#         min = i
#         print(min)
#         break



#B
# sum = 0

# while True:
#     x = int(input())
#     sum += x
#     if x == 0:
#         print(sum)
#         break


#A
# x = int(input())
# y = int(input())
# cnt = 1
# while y - x >= 0:
#     x = x + (x * 0.2)
#     cnt = cnt + 1


# print(cnt)



#B
# cnt = 0
# while True:
#     x = int(input())
#     if(x % 2 == 0):
#         cnt += 1
#         if(x == 0):
#             break
# print(cnt-1)


      
#A
# cnt = 0
# y = float("inf")

# while True:
#     x = int(input())
#     if x>y:
#         cnt+=1
#     y = x
#     if x ==0:
#         print(cnt)
#         exit()


#B
# mx  = -float("inf")
# smx = -float("inf")
# while True:
#     x = int(input())
#     if x > mx :
#         smx = mx 
#         mx = x
#     elif x >smx:
#         smx = x    
#     if x ==0:
#         print(smx)
#         exit()