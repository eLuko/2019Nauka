conc_a = 35
conc_b = 20
a = conc_a
b = conc_b

#for i in range(1,400):
while True:
    if a > b:

        b = b + conc_b
        if a==b:
            break
    else:
        a = a + conc_a

   # print ("a "  + str(a))
   # print ("b " + str(b))
    if a == b:
        break

print(b)

