import string
x=str(input('Введите Ф.И.О. '))
for item in string.digits:
    x=x.replace(item, ' ')

while '  ' in x:
    x=x.replace('  ', ' ')
print(x.title())


