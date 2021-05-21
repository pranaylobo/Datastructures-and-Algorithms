# Time Complexity	 
# Best	O(n)
# Worst	O(n2)
# Average	O(n2)

arr = [-2, 45, 0, 11, -9]


count = 0

while count!=len(arr):


    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]

    count = count + 1

print(arr)