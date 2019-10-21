
def partition(arr,low,high):
    #indexPivot=len(arr)//2
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    print (pivot)
    for j in range (low, high):
        print('-------------')
        #print(pivot)
        if arr[j] <= pivot:
            print(arr[j])
            print(arr[i+1])
        # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

        #arr[0],arr[4]=7,9
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(i+1)
    return (i+1)
arr1=[1,9,3,3,3,2,4,5,7,8,6,3]
n=len(arr1)
partition(arr1,0,n-1)
print(arr1)
partition(arr1,3,n-1)
print(arr1)



arrtest=[4,1,3]
pivot=arrtest[0]
less = [k for k in arrtest[1:] if k<= pivot]
for i in arrtest[1:]:
    if i<= pivot:
        print(i)
print(less)
'''
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        print (arr)
        quickSort(arr, pi+1, high)
        print (arr)


arr = [1,9,2,4,5,7,8,6,3]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [1,9,2,4,5,7,8,6,3]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),'''