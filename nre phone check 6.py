import re

print('Entry:')

entry = input()

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

match_object = phone_num_regex.findall(entry)

print(match_object.group())
