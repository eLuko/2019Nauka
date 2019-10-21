def helloWorld(vNumber,d=2):
    return vNumber/d
xx=helloWorld(12,4)
sortedList=[1,2,3,4,5,6,7,8,9]
#print(len(sortedList))
low=0
high=len(sortedList)-1
#mid=high / 2
szukana=19
#print(int(mid))

while low<=high:

    mid = int ((high + low) / 2)
    quess = sortedList[mid]
    print(quess)
    szu =-1
   # print(quess)
    if szukana==quess:
        szu=sortedList[mid]

        break
    if szukana<quess:
        high=mid-1

        print(high)
    else:
        low  = mid+1
        print('low')
print('----------------')
print(szu)



'''
def binary_search(item_list, item):
    first = 0
    last = len (item_list)
    print(last)
    found = False
    while (first <= last and not found):

        mid = int((first + last) / 2)
        print('+++++')
        print(first)
        print(last)
        print('mid')
        print(mid)

        if item_list[mid] == item:
            found = True
            print(item_list[mid] )
        else:
            if item < item_list[mid]:
                last = mid - 1
                print('last')
                print(last)
            else:
                first = mid + 1
                print('first')
                print(first)
    return found


#print (binary_search ([1, 2, 3, 5, 8], 6))
print (binary_search ([1, 2, 3, 5, 8,9,10], 8))
'''