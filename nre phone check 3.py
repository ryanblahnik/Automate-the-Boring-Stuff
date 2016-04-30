def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' and text[3] != '.':
        return False
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-' and text[7] != '.':
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Entry:')

entry = input()

found_number = False
for i in range(len(entry)):
    chunk = entry[i:i+12]
    if is_phone_number(chunk) == True:
        print('Found: ' + chunk)
        found_number = True
if not found_number:
    print('No returns found.')
