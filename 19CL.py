import re 


#Easy A
# txt = input()

# pat =  '[0-9]'

# res = re.findall(pat,txt)
# print(res)
# if res:
#     print(True)
# else:
#     print(False)


#Easy B
# txt = input()

# pat =  '[A-Za-z, 0-9]'

# res = re.findall(pat,txt)
# print(res)
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

#Easy C
# txt = input()

# pat =  '[A-Z][a-z]+'

# res = re.findall(pat,txt)
# print(res)
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

#Medium A
# txt = input()

# res = re.findall(r'cool+$',txt)
# print(res)
# if res:
#     print(True)
# else:
#     print(False)

#Medium B
# txt = input()

# pat =  '.*a.*b$'

# res = re.findall(pat,txt)
# print(res)
# if res:
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")

#Medium B
# txt = input()

# pat =  r"^[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}$"

# res = re.findall(pat,txt)
# print(res)
# if res:
#     print("IP")
# else:
#     print("Something else")

#Hard A
# txt = input()

# pat =  "^[78][0-9]{3}[0-9]{7}$"

# res = re.findall(pat,txt) 
# print(res)
# if res:
#     print("Call me maybe")
# else:
#     print("Something else")

#Hard B


#HW 19
#Easy A
# txt =input()
# pat = '([0-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-([1][0-9]{3}|[2][0][0-2][0-9]|[0-9]{1,3})'
# res=re.findall(pat,txt)
# for i in res:
#     print('{}-{}-{}'.format(i[0],i[1],i[2]))

#Easy B
# def vowel(txt):
#     pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
#     vowel_words = re.findall(pattern, txt)
#     return vowel_words

# txt = input()
# vowel_words = vowel(txt)
# print(vowel_words)

#Medium A
# def check(txt):
#     pattern = re.compile(r'\d+$')
#     return bool(pattern.search(txt))

# txt = input()
# print(check(txt))

#Medium B
# txt =input()

# pat = '[0-9]'
# res=re.search(pat,txt)

# print(res.group(0))
# print(res.start())

#Hard A
# txt = input()

# res = re.findall(r"\b\w{5}\b",txt)

# print(res)

#Hard B
# txt =input()


# pat = '([a-zA-Z])([A-Z])'


# res=re.sub(pat,r'\1_\2_\3',txt)

# print(res)