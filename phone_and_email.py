#! python3

import re, pyperclip

# TO DO: Create a regex for phone numbers

phone_re = re.compile(r'''

# xxx-xxx-xxxx,
# xxx-xxxx,
# (xxx) xxx-xxxx
# ext xxxxx
# ext. xxxxx
# x xxxxx
# xxxxxx

# area code (optional)
# first separator
# exchange
# separator
# local digits
# extension (optional)

(
((\d\d\d)|(\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s)|x(\s)?)
(\d{2,5}))?
)

''', re.VERBOSE)

# TO DO: Create a regex for email addresses

email_re = re.compile(r'''

#x@y.zzz, inc !#$%^&*'-_+=/?{}|`~

# name
# @
# domain

([a-zA-Z0-9!#$%^&*'_+=/?{}|`~]+
@
[a-zA-Z0-9!#$%^&*'-_+=/?{}|`~]+
.
[a-zA-Z0-9!#$%^&*'_+=/?{}|`~]+)

''', re.VERBOSE)

# NOTE: INCLUDING - in email.re RETURNED SURROUNDING PARENTHESES




# TO DO: Get the text off the clipboard

text = pyperclip.paste()

# TO DO: Extract the info from this text

extr_p = phone_re.findall(text)
extr_e = email_re.findall(text)

all_phone = []
for phone in extr_p:
    all_phone.append(phone[0])

# TO DO: Copy the info to the clipboard

final = '\n'.join(all_phone) + '\n' + '\n'.join(extr_e)

pyperclip.copy(final)

print(final)
