#A
#a = (str(input()))
#if(a == 'Бонд'):
#    print("Добро пожаловать мистер Бонд")
#else:
#    print("Добро пожаловать на борт")



#B
#a = (int(input()))
#if(a % 2 == 0):
#    print("Even")
#else:
#    print("Odd")



#C
#a = (float(input()))
#b = (float(input()))
#if(a>b):
#    print(a)
#elif(a<b):
#    print(b)
#else:
#    print("EQUAL")



#A
#a = (int(input()))
#b = a % 100
#if(b > 1):
#    print("good")
#else:
#    print("not bad")



#B
#a = (str(input()))
#if(ord(a) > 96 and ord(a) < 123):
#    print("SMALL")
#elif(ord(a) < 91 and ord(a) > 64):
#    print("big")
#else:
#    print("error")


#C
#a = (int(input()))
#if(a == 0):
#    print("zero")
#elif(a == 1):
#    print("one")
#elif(a == 2):
#    print("two")
#elif(a == 3):
#    print("three")
#elif(a == 4):
#    print("four")
#elif(a == 5):
#    print("five")
#elif(a == 6):
#    print("six")
#elif(a == 7):
#    print("seven")
#elif(a == 8):
#    print("eight")
#elif(a == 9):
#    print("nine")



#A
#a = (int(input())) 
#b = (int(input()))
#c = (int(input()))
#d = (int(input()))

#if(a and b > 0 and c and d < 0):
#    print("its ok")
#elif(a and c > 0 and d and b < 0):
#    print("its ok")
#elif(a and d > 0 and c and b < 0):
#    print("its ok")
#elif(c and b > 0 and a and d < 0):
#    print("its ok")
#elif(d and b > 0 and c and a < 0):
#    print("its ok")
#elif(c and d > 0 and a and b < 0):
#    print("its ok")
#else:
#    print("oh no")



#B
#a = (int(input()))
#if((a % 4 == 0 and a % 100 != 0) or (a %400 == 0)):
#    print("leap year")
#else:
#    print("common")




#3HW
#A
#a = int(input())
#b = str(input())
#print(type(a))
#print(type(b))


#B
#a = (int(input()))
#b = (int(input()))
#c = (int(input()))
#if(a * b == c):
#    print("true")
#else:
#    print("false")



#A
#a = (int(input()))
#b = (int(input()))
#if(a and b > 0):
#    print("Both numbers are greater than zero")
#elif(a or b > 0):
#    print("One number is greater than zero")
#else:
#    print("Both numbers are less than zero")


#B
#a = (int(input()))
#b = (int(input()))
#c = (int(input()))
#if(a < b and a < c):
#    print(a)
#elif(b < c and b < a):
#    print(b)
#else:
#    print(c)


#A
#a = (int(input()))
#b = (int(input()))
#c = (int(input()))
#d = (int(input()))
#e = c - a
#f = d - b
#if(f < 0):
#    print(abs(e - 1), abs(f), sep=' ')
#else: 
#    print(e, f, sep=' ')


#B
#a = (int(input()))
#if(a == 1):
#    print(a,"утка", sep=' ')
#elif(a == 2 or a == 3 or a ==4):
#    print(a,"утки", sep=' ')
#else:
#    print(a,"уток", sep=' ')
