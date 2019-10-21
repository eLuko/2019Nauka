def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

def fractional(i):
    if i==0:
        return 1
    else:
        return i * fractional(i-1)

countdown(6)
print(fractional(3  ))