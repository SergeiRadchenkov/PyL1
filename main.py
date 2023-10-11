n = None
print(n)

n = 'fghh\'dgjj'
print(type(n))
print(n)
# print(n)
"""
gddfhfgjfj
"""

a = 5
b = 5.89
c = 'hello'

print(a, ' - ', b, ' - ', c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a, b, c))

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, '+' , b, '=' , a + b)

c = 1
print(c)
print(type(c))
c = bool(c)
print(c)
print(type(c))

a = 5.5645
b = 4.54654
print(round(a*b, 3))

a = 1 > 4
print(a)
a = 1 < 4 and 5 > 2
print(a)
a = 1 == 2
print(a)
a = 1 != 2
print(a)
a = 'qwe'
b = 'qwe'
print(a == b)
a = 1 < 3 < 5 < 10
print(a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - ТОП)')
# else:
#     print('Привет,', username)

i = 0
while i < 5:
    # if i == 3:
    #     break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать число, делённое на 2
#         print(n)
#         flag = False
#     i += 1

a = 'qwerty'
# print(a[0])
for i in a:
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text))
print('ещё' in text)
print(text.lower())
print(text.upper())
print(text.replace('ещё', 'ЕЩЁ'))

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(text[0]) # С
print(text[1]) # ъ
print(text[len(text)-1]) # к     
print(text[-5]) # к
print(text[-5]) # б
print(text[:]) # СъЕШЬ ещё этих МяГкИх французских булок
print(text[:2]) # Съ
print(text[-5:]) # Съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ЕШЬ ещё
print(text[6:-18]) # ещё этих МяГкИх
print(text[0:len(text):6]) # Сеикакл
print(text[::6]) # Сеикакл
text = text[2:9] + text[-5] + text[:2]
print(text)