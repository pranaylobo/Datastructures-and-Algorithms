matrix =[]
matrixdict = {}
arrkeys=[]
admatrix=[]
index12={}
visited=[]
class Node:
    def __init__(self,value):
        self.value = value
        matrix.append(value)

        


class Graph:
    def __init__(self):

        for i in range(0,len(matrix)):

            if matrix[i][1] not in arrkeys:
                arrkeys.append(matrix[i][1])

            if matrix[i][0] not in arrkeys:
                arrkeys.append(matrix[i][0])
            arrkeys.sort()
            # print(arrkeys) #keys -->0,1,2,3,4


        for k in arrkeys:
            matrixdict.update({k:[0,0,0,0,0]}) #adjecencymatrix initialized

    
        for index,k in enumerate(matrix):
            temp =[]

            temp=matrixdict.get(k[0])
            tempo =k[1]            

            temp[tempo] =1



        for j in range(0,len(matrixdict)):

            array =[]

            array = matrixdict.get(j)

            for index,value in enumerate(array):
                newtemp=[]
                if value == 1:

                    newtemp = matrixdict.get(index)
                    newtemp[j] = 1
        # Adjecency Matrix

        print("Adjecency Matrix")

        for j in range(0,len(matrixdict)):

            array =[]

            array = matrixdict.get(j)

            print(array)


        # Simple Graph Traversal

        for j in range(0,len(matrixdict)):

            array =[]

            array = matrixdict.get(j)

            print(array)

            for index,value in enumerate(array):
                if value == 1 and index not in visited:
                    visited.append(index)





        print("Nodes in graph")
        visited.sort()
        print(visited)



e1 = Node([0, 1]) 
e2 = Node([0, 4]) 
e3 = Node([1, 2]) 
e4 = Node([1, 3]) 
e5 = Node([1, 4]) 
e6 = Node([2, 3]) 
e7 = Node([3, 4])
e8 = Graph() 
  
