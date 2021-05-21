
def main(n):

    if n ==0 or n ==1:
        return n

    else:
        return(main(n-1)+main(n-2))




def input1():
    n = 10
    for i in range(n):
       print(main(i))
    

input1()