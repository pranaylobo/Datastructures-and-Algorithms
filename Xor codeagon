#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(x, l, r):
    # print(x,l,r)
    
    store =[]
    count=0
    for i in range(l,r+1):
        temp=x^i
        
        count=count+1
        range1 = (r-l)+1
        
        if count == range1:
            
            if temp > store[0]:
                store[0] = temp
                return store[0]
            
            else:
                return store[0]
                store.pop()
            
        else:
            
            if len(store) ==0:
                store.append(temp)

            elif temp > store[0]:
                store[0] = temp
            
        
            
    
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        xlr = input().rstrip().split()

        x = int(xlr[0])

        l = int(xlr[1])

        r = int(xlr[2])

        result = solve(x, l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(x, l, r):
    # print(x,l,r)
    
    store =[]
    count=0
    for i in range(l,r+1):
        temp=x^i
        
        count=count+1
        range1 = (r-l)+1
        
        if count == range1:
            
            if temp > store[0]:
                store[0] = temp
                return store[0]
            
            else:
                return store[0]
                store.pop()
            
        else:
            
            if len(store) ==0:
                store.append(temp)

            elif temp > store[0]:
                store[0] = temp
            
        
            
    
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        xlr = input().rstrip().split()

        x = int(xlr[0])

        l = int(xlr[1])

        r = int(xlr[2])

        result = solve(x, l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
