class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right =None 

class tree:

    def __init__(self,root=None):
        self.root = root
        self.count = 0

        self.current = self.root
        self.newcurrent=None
        self.newcurrent1=None



    def definetree(self,newelement=None):
        
        
        print("count",self.count)
        if self.count <=1:

            if newelement.value < self.current.value:
                self.current.left = newelement
                self.count =self.count+1

            elif newelement.value > self.current.value:
                print("dddd")
                self.current.right = newelement
                self.count =self.count+1

        else:

            if newelement.value < self.current.value:
                self.newcurrent = self.current.left

                if newelement.value < self.newcurrent.value:
                    self.newcurrent.left = newelement

                if newelement.value > self.newcurrent.value:
                    self.newcurrent.right = newelement

                    

                

            else:
                print("else")
                
                if newelement.value > self.current.value:
                    self.newcurrent1 = self.current.right



                    if newelement.value < self.newcurrent1.value:
                        self.newcurrent1.left = newelement

                    if newelement.value > self.newcurrent1.value:
                        self.newcurrent1.right = newelement



    def printtree(self):
        print("root,root->left,root->right",self.current.value, self.current.left.value,self.current.right.value,self.newcurrent.left.value,self.newcurrent.right.value,self.newcurrent1.left.value,self.newcurrent1.right.value)


    def search(self,key):
        # VLR preorder
        print("key",key)

        if key == self.current.value:
            print("Found")

        else:

            
            if key > self.current.value:
                root = self.current.right

            elif key < self.current.value:
                root = self.current.left

            print("newroot",root.value)

            if root.left.value == key:
                print("Found")

            elif root.right.value == key:
                print("Found")

            elif root.value == key:
                print("Found")

            else:
                print("NotFound")


        




    

        
e1 = Node(8)
e2 = Node(12)
e3 =Node(10)  #Root

e4 = Node(6)
e5 = Node(9)

e6 = Node(11)
e7 = Node(13)

t1 = tree(e3)
t1.definetree(e1)
t1.definetree(e2)
t1.definetree(e4)
t1.definetree(e5)
t1.definetree(e6)
t1.definetree(e7)
t1.search(8)
t1.printtree()

# output
# Found
# root,root->left,root->right 10 8 12 6 9 11 13
