listOfNumber=[]
#listOfNumber=[2,3,4,5,6,7,8,9]
for i in range(2,10001):
    listOfNumber.append(i)

naturalNumber=[]
print(naturalNumber)
dnumr=1
i=0
while i < len(listOfNumber):
 naturalNumber.append(listOfNumber[i])
 aa = listOfNumber[i]
 for z in listOfNumber[:]:
   # print('z')
    #print(z)
    #print(listOfNumber.index(z))
    #print('end z')
    xmod=z%aa
    if int(xmod)==0:

        listOfNumber.remove(z)

        #del listOfNumber[listOfNumber.index(z)]


print(naturalNumber)
#print(listOfNumber)

print(3%3)




