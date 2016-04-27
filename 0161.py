import pprint

message = 'There ain\'t nothin you would ask I could answer you that I won\'t.. but I was gonna change and I\'m not if you keep doin things I don\'t'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(message)
pprint.pprint(count)
 
    
