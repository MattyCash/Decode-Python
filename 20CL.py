#20CL
import re
#Easy A
# txt =input()

# pat = r'[0-9]'

# res = re.sub(pat,'',txt)
# print(res)  

#Easy B
# txt = input()

# pat = '[ ,.]'

# res = re.split(pat, txt)
# print(res)

#Easy C
# txt = input()

# pat = r'^the'

# if re.match(pat, txt):
#    print("Exist")
# else:
#     print("Ne exist")
    
#Medium A
# txt = input()

# pat = r'decode'

# res=re.search(pat,txt) 

# if re.search(pat,txt):
#     print("Exist")
#     print(res.start())
#     print(res.end())
# else:
#     print("ne exist")

#Medium B
# txt = input().lower()

# pat = '^(http|https)://[a-z]+[.][a-z]+/?$'

# res = re.search(pat,txt)

# if res:
#     print(1==1)
# else:
#     print(1==0)

#Medium C
# txt = input()

# pat = r'\b[A-Z][a-z]+\b'

# res = re.findall(pat, txt)
# print(res)

#Hard A
# txt = input()

# pat = '^[a-z0-9._]+@[a-z]{2,6}[.][a-z]{2,4}$'

# res = re.findall(pat,txt)

# if res:
#     print(1==1)
# else:
#     print(1==0)
#Hard B

#20HW
txt = input()

rgb_pat = r'^rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)$'

hsl_pat = r'^hsl\((\d{1,3}), (\d{1,3})%, (\d{1,3})%\)$'

if re.match(rgb_pat, txt):
    r, g, b = map(int, re.findall(rgb_pat, txt)[0])
    if r == g == b:
        print('YES')
    else:
        print('NO')

elif re.match(hsl_pat, txt):
    h, s, l = map(int, re.findall(hsl_pat, txt)[0])
    if s == 0 and l == 75:
        print('YES')
    else:
        print('NO')

else:
    print('NO')