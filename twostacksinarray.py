
elements = int(input("Enter Number of Elements"))
arr=[]
start=0


def push(arr,start,mid,end):

    if len(arr)==0:
        x=input("")
        arr.append(x)
        start = start+1
        main()

    else:

        while start != mid:
            for i in range(start,mid):
                x = input("")
                arr.append(x)

                start = start+1

        print("Stack 1 is full")

        print("Checking Stack 2")

        while mid+1 != end:

            print("Pushing to stack 2")
            for i in range(mid+1,end):
                x = input("")
                arr.append(x)

                end = end-1

        print("Stack 2 is full")


    print(arr)

def main():
    

    mid = elements//2

    
    end= elements


    push(arr,start,mid,end)

main()






    
    