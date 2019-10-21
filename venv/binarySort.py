def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            print(arr[i])
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest =findSmallest(arr)
        newArr.append(arr.pop(smallest))
       # print(smallest)
    return  newArr
arr1=[4,6,2,3,5]
pom=selectionSort(arr1)
print(pom)
# Znajduje najmniejszą wartość w tablicy
'''def findSmallest(arr):
  # Przechowuje najmniejszą wartość.
  smallest = arr[0]
  # Przechowuje indeks najmniejszej wartości.
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      print(arr[i])
      smallest_index = i
  return smallest_index

# sortuje tablicę
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Znajduje najmniejszy element w tablicy i dodaje go do nowej tablicy.
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr
'''
print (selectionSort([4,6,2,3,5]))
