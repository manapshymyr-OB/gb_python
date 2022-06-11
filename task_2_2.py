"""2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']"""

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
import re
new_lst = []
symbol = None
for digit in lst:

    if digit[0] in '+-':
        symbol = digit[0]
        digit = digit[1:]

    if digit.isdigit() == True:
        digit = digit.zfill(2)
        if symbol is not None:
            digit  = symbol + digit.zfill(2)
        new_lst.append('"')
        new_lst.append(digit)
        new_lst.append('"')

    else:

       new_lst.append(digit)


odd = 0
new_str = ''
for i in new_lst:

    if '"' in i:
        odd+=1
        print(odd)
        if odd % 2 == 0:
            new_str = new_str.strip()
            new_str += i + " "
        else:
            print(new_str)
            new_str += i

    else:
        new_str += i + " "



print(new_str)
