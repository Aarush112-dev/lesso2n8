class Node():
    def __init__(self,value):
        self.value = value
        self.left = ""
        self.right = ""
    
def preorder(parent): #root-left-right
    if parent:
        print(parent.value)
        preorder(parent.left)
        preorder(parent.right)

def postorder(parent): #left-right-root
    if parent:
        postorder(parent.left)
        postorder(parent.right)
        print(parent.value)

def inorder(parent): #left-root-right
    if parent:
        inorder(parent.left)
        print(parent.value)
        inorder(parent.right)

parent = Node(72)
parent.left = Node(9)
parent.right = Node(8)
parent.left.left = Node(3)
parent.right.left = Node(4)
parent.right.right = Node(2)
parent.right.left.left = Node(1)
parent.right.left.right = Node(5)
print("preorder")
preorder(parent)
print("postorder")
postorder(parent)
print("inorder")
inorder(parent)

while True:
    question = input("1) Create a Tree and Insert nodes \n2) Preorder Traversal \n3) Inorder Traversal \n4) Postorder Traversal \n5) Exit \nAnswer= ")

    if question == "1":
        parent_question = input("Value of parent: ")
        parent_right_question = input("Value of right parent: ")
        parent_left_question = input("Value of left parent: ")
        a = input("Value of children node of right parent: ")
        a2 = input("Second value of children node of right parent: ")
        b = input("Value of children node of left parent: ")
        b2 = input("Second value of children node of left parent: ")

        parent = Node(parent_question)
        parent.right = Node(parent_right_question)
        parent.left = Node(parent_left_question)
        parent.right.right = Node(a)
        parent.right.left = Node(a2)
        parent.left.right = Node(b)
        parent.left.left = Node(b2)

    if question == "2":
        preorder(parent)

    if question == "3":
        inorder(parent)

    if question == "4":
        postorder(parent)

    if question == "5":
        print("The program has been exited")
        break
    


        