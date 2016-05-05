'''

***********
*         *
*         *
*         *
***********


'''


def box_print(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('''
********
**  **
**  **
******** box when symbol > 1 character''')
    if (width <2) or (height <2):
        raise Exception('''That's a line, not a box''')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

box_print('*', 50, 7)
box_print('~', 58, 20)

print('Symbol?')

s = input()

print('Width?')

w = input()

print('Height?')

h = input()

box_print(s, int(w), int(h))
