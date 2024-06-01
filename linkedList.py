class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class linkedList: 
    def __init__(self): 
        self.head = None 
    
    def add(self, data): 
        
        newNode = Node(data) 
        
        if self.head is None: 
            self.head = newNode 
            return 
        
        last = self.head 
        while last.next is not None: 
            last = last.next 
        last.next = newNode          
        
    def traverse(self): 
        currentNode = self.head 
        
        while currentNode is not None: 
            print(currentNode.data, end=" -> " ) 
            currentNode = currentNode.next 
        print("None")


       
            
mylinkedlist = linkedList() 
mylinkedlist.add("A")
mylinkedlist.add("B")
mylinkedlist.add("C")

mylinkedlist.traverse()


 
  