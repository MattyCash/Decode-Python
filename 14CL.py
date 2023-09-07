#2D arrays HW
#A Easy 
# n,m = map(int,input().split())

# a=[]

# for i in range(n):
#     b= list(map(int,input().split()))
#     a.append(b)

# mx= a[0][0]
# idx=0
# jdx=0

# for i in range(n):
#     for j in range(m):
#         if mx < a[i][j]:
#             mx = a[i][j]
#             idx = i
#             jdx = j


# print(idx,jdx)

#A Medium



#A Hard
# n = int(input())
# # 
# # a= [['.']*n]*n
# a=  [['.' for i in range(n)] for j in range(n)]

# for i in range(n):
#     a[n//2][i]='*'  # горизонтальная
#     a[i][n//2]='*'   # вертикальная
#     a[i][i] = '*'    # диагональная слева сверху на право вниз
#     a[i][n-i-1] = '*'  # диагнольная справ сверху в лево на низ










# for i in range(n):
#     for j in range(n):
#         print(a[i][j],end="")
#     print()
