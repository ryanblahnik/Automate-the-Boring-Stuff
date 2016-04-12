print('What is your name?')
name = input()
print(name + ', are you tired?')
tired = input()
if tired == 'yes':
    print('In that case, you should probably go to bed, ' + name)
elif tired == 'Yes':
    print('In that case, you should probably go to bed, ' + name)
elif tired == 'Y':
    print('In that case, you should probably go to bed, ' + name)
elif tired == 'y':
    print('In that case, you should probably go to bed, ' + name)
elif tired == 'No':
    print('CRANK IT UP')
elif tired == 'n':
    print('CRANK IT UP')
elif tired == 'N':
    print('CRANK IT UP')
elif tired == 'no':
    print('CRANK IT UP')
else:
    print('what are you speaking')
