#! python3

import random

heads = 0

for i in range(1, 100001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 50000:
            print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')

            
