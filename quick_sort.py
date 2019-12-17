import random
k = 0
def partition(lst, low, high):
    global k
    i = (low -1)
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1],lst[high] = lst[high], lst[i+1]
    k+=1
    print("Round %d" %k)
    print(lst)
    return (i+1)
            
def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi-1)
        quick_sort(lst, pi+1, high)
 
arr = []
size = int(input("Enter size of the list: "))

arr = [random.randint(1,1000) for _ in range(size)]
 
low = 0
high = len(arr) - 1
quick_sort(arr, low, high)
print("---Final Result----")
print(arr)