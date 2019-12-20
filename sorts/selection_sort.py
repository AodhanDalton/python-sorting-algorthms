import sys
import random
import time

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   END = '\033[0m'

usr = input("Size of array: ")

# creating an array of the size the user has entered with random numbers from 1,1000
arr = [random.randint(1,1000) for _ in range(usr)]

# for loop with the selection sort inside it
print(color.GREEN + "Size %d" %usr)

for i in range (len(arr)):

    min = i
    for j in range (i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j

    # swapping the values 
    arr[i], arr[min] = arr[min], arr[i]
    tmp = arr[i]
    # Print statment for the end of each loop
    print ("\nRound %d" %(i+1))
    for i in range (len(arr)):
        if(arr[i] == arr[min]):
            print(color.RED + '%d' %arr[i] + color.END),
            time.sleep(.05)
        elif(arr[i] == tmp):
            print(color.GREEN + '%d' %arr[i] + color.END),
            time.sleep(.05)
        else:
            print ("%d" %arr[i]),
            time.sleep(.05)

# Printing the value of the sorted array 
print ("\n===============")
print ("Sorted array") 
for i in range(len(arr)): 
    print("%d" %arr[i]),
print ("\n===============")
