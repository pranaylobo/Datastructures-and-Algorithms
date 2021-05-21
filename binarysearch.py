

def binarysearch(arr,x,low,high):

    mid =low + (high - low)//2
    data=x

    if high >= low:
        if arr[mid] ==x:
            return mid

        else:
            if x > arr[mid]:
                return binarysearch(arr,x,mid+1,high)

            else:
                return binarysearch(arr,x,low,mid-1)



    else:
        return -1



arr=[1,2,3,4,5,6]

x = 1

high = len(arr)-1

result = binarysearch(arr,x,0,high)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")