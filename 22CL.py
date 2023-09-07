# #Easy A
# class Point:
#     def init(self,x=5,y=10):
#         self.x = x
#         self.y = y
    

# p1=Point()
# var = input()

# if var == 'x':
#     print(p1.x)
# else:
#     print(p1.y)


# #Easy B
# class Point:
#     def init(self,x=5,y=10):
#         self.x = x
#         self.y = y
    

# x =int(input())
# y =int(input())

# p1=Point(x,y)
# var = input()

# if var == 'x':
#     print(p1.x)
# elif var == 'y':
#     print(p1.y)

# #Easy C
# class Point:
#     def init(self,x=5,y=10):
#         self.x = x
#         self.y = y
#     def dist(self,p2):
#         return ((p2.x-self.x)**2+(p2.y-self.y)**2)**0.5


# x1 =int(input())
# y1 =int(input())
# x2 =int(input())
# y2 =int(input())

# p1=Point(x1,y1)
# p2=Point(x2,y2)


# print(p1.dist(p2))

#Meduim A
# class Rect:
#     def init(self,a,b):
#         self.a = a
#         self.b = b
#     def is_square(self):
#         return self.a == self.b


# a=int(input())
# b=int(input())


# r1=Rect(a,b)

# print(r1.is_square())

#Meduim B
# class Rect:
#     def init(self,a,b):
#         self.a = a
#         self.b = b
#     def is_square(self):
#         return self.a == self.b
#     def get_diagonal(self):
#         return (self.a**2 + self.b**2)**0.5
#     def get_perimeter(self):
#         return 2*(self.a + self.b)
#     def get_area(self):
#         return self.a * self.b

# a=int(input())
# b=int(input())


# r1=Rect(a,b)

# print(r1.is_square())
# print(r1.get_area())
# print(r1.get_diagonal())
# print(r1.get_perimeter())


#Hard A
# id =1

# class Shop:
#     products  = {
#                 'Milk':300,
#                 'Meat':3000, 
#                 'Chocolate':500,
#                 'bread':120
#                 } 
#     def init(self,name):
#         global id
#         self.id = id
#         id +=1
#         self.name = name
#         self.cart = {}

#     def buy(self, nameofproduct,quantity):
#         if self.products.get(nameofproduct) != None:
#             self.cart[nameofproduct]= quantity
#         else :
#             print("Нету такого продукта")
    
#     def show_cart(self):
#         print()
#         for product, quantity in self.cart.items():
#             print(product ,":", quantity)
#         print()
#     def total_sum_of_products(self):
#         self.total =0
#         for product, quantity in self.cart.items():
#             self.total +=(self.products[product]*quantity)
#         return self.total


# s1=Shop("Maksat")
# s2=Shop("Dinara")


# s1.buy('Meat',3)
# s2.buy('Chocolate',1)
# s2.buy('Ch',1)



# s1.show_cart()
# s2.show_cart()


# s1.buy('Milk',2)
# s2.buy('bread',3)


# s1.show_cart()
# s2.show_cart()


# print(s1.total_sum_of_products())
# print(s2.total_sum_of_products())