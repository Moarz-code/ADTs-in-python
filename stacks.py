class stack: 
    def __init__(self): 
        self.items = []
    
    def push(self, data):  
        self.items.append(data)
    
    def pop(self): 
        if not self.is_empty(): 
            return self.items.pop()
        return None 
    

myStack = stack() 

myStack.push("A")
myStack.push("B")
myStack.push("C")

#Print the stack 
print("Stack: ", myStack.items)




         