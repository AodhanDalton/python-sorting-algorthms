def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range (0, n-i-1):
           
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1,23,4,2,12,54]

bubblesort(arr)
print ("Sorted array:")
for i in range (len(arr)):
    print ("%d" %arr[i]),