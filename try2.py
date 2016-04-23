print('How many cats do you have?')
num_cats = input()
try:
    if int(num_cats) >=4:
        print('That\'s a lot of cats.')
    elif int(num_cats) < 0:
        print('That\'s an unlikely number of cats.')
    else:
        print('That is not that many cats.')
except:
    print('What are you trying to achieve here?')
