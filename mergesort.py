

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right= arr[mid:]

        mergesort(left)
        mergesort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] <right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1

            k+=1

        while i <len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        # while j <len(right):
        #     arr[k] = left[j]
        #     j+=1
        #     k+=1

    
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()    


def input1():
    arr=[1,4,2,36,9]

    mergesort(arr)

    printList(arr)

input1()