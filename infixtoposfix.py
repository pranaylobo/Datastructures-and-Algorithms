
import re

a = input()

arr = a.split()
print(arr)

stack =[]
output=[]


# x = re.search("[^A-Za-z][Tt]he[^A-Za-z]")


def divide(stack,output,length):

    if (stack[length-1] == "/") or (stack[length-1] == "*") or (stack[length-1] == "^"):
                x=stack.pop(length-1)
                output.append(x)

    len1=len(stack)-1
    
    if (stack[length-1] == "/") or (stack[length-1] == "*") or (stack[length-1] == "^"):
        add(stack,output,len1)


def add(stack,output,length):
    if (stack[length-1] == "/") or (stack[length-1] == "-") or (stack[length-1] == "*") or (stack[length-1] == "^") or (stack[length-1] == "+"):

        x=stack.pop(length-1)
        output.append(x)
        
    len1=len(stack)-1
    
    if (stack[len1-1] == "/") or (stack[len1-1] == "-") or (stack[len1-1] == "*") or (stack[len1-1] == "^") or (stack[len1-1] == "+"):
        add(stack,output,len1)



for i in arr:
    x=re.match("[A-Z]",i)

    y =re.match("[(+*-/^)]",i)

    z = re.match("[()]",i)

    if x:

        output.append(i)

    if y:

        
        stack.append(i)
        length = len(stack)-1
        if i == "+" or i =="-":
            add(stack,output,length)
            

            
        
                

        if i == "/" or i =="*":

            divide(stack,output,length)

            

        if i == ")":

            count = stack.index(i)
            stack[count]=""

            while stack[count] !="(":
                
                count = count-1

                y =re.match("[+*-/^]",stack[count])

                if y:
                    output.append(stack[count])
                    stack[count]=""

            
            stack[count]=""
            stack = list(filter(None, stack))


         


print("Output",output)







