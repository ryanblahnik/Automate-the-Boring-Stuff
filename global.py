def spam():
    global eggs
    eggs = 43
    print(eggs)

eggs = 42
spam()
print(eggs)
