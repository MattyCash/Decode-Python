#Dictionary

#A Easy
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# d = {}

# for i in range (len(keys)):
#     d[keys[i]] = values[i]

# print(d)

#B Easy
# sampleDict = {
#     "class":{
#         "name":"Mike",
#         "marks": {
#             "physcis": 70,
#             "history": 80
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

#C Easy
# sample_dict = {
#     'Physics': 82,
#     'Math': 65,
#     'History': 75
# }
# mn = 1000000000

# for i in sample_dict.values():
#     mn = min(i,mn)
    
# for k in sample_dict.keys():
#     if(sample_dict[k] == mn):
#         print(k)
#         break

#D Easy
# info = {'name' : 'Aidana', 'grades' : [96,78,67,73,90]}
# s=sum(info['grades'])/len(info['grades'])
# print(s)

#A medium
# n = int(input())

# d ={}

# for i in range(n):
#     name,grade = input().split()
#     d[name] = int(grade)

# print('name | grades')

# for k in sorted(d.keys()):
#     print(k,':',d[k])

#B Medium
# a = input().split()

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] =1

# for k in sorted(d.keys()):
#     print(k, d[k])

#C Medium
# a = input()

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i] =1

# for k in sorted(d.keys()):
#     print(k, d[k])

#A Hard
# n =int(input())

# d={}

# bank=0

# for i in range(n):
#     name,money=input().split()
#     if name not in d:
#         d[name] =int(money)
#     else:
#         d[name]+=int(money)
#     bank+=int(money)



# for k in sorted(d.keys()):
#     percent = (d[k]/bank)*100
#     print(k , f'{percent}%')

#B Hard



#Dictionary

#A Easy
# a=int(input())
# b=int(input())
# d={}
# for i in range(a,b+1):
#     d[i] = i**2

# print(d)



#B Easy
# d = {
#  "OOP":[77,88,99,66],
#  "ICT":[100,98,99,96]
# }
# for k ,v in d.items():
#     for v1 in v:
#         print(k,":",v1)


#A Medium
# a= input().split()
# d={}
# for i in a:
#     if i in d:
#         print(d[i],end=" ")
#         d[i]+=1
#     else: 
#         print(0,end=" ")
#         d[i] = 1

#B Medium
# s= input()
# d={}
# for i in s:
#     if i.isalpha():
#         if i in d:
#             d[i]+=1
#         else:
#             d[i] = 1

# print(d)


#A Hard
# n = int(input())
# d={}
# for i in range(n):
#     country,*cities = input().split()
#     d[country] = cities


# n = int(input())
# for i in range(n):
#     city = input()
#     for country,cities in d.items():
#         if city in cities:
#             print(country)
#             break 
    
#B Hard
# n = int(input())
# d={}
# for i in range(n):
#     s1,s2=input().split()
#     d[s1] = s2
#     d[s2] = s1


# s= input()

# print(d[s])