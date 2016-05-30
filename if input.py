print('WELCOME')
x = input()
def f(x):
    if int(x) > 0:
        x = int(x) * 10
        print("Take " + str(x))
    if int(x) <= 0:
        x = int(x) * 10
        x = x * -1
        x = x + 10
        print("Take " + str(x))
    if int(x) == None:
        print("How many rats are you looking for?")
        y = input()
        f(y)
f(x)
print('Now go on.')


    
