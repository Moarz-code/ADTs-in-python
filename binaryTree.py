class Node: 
    def __init__(self): 
        self.left = None 
        self.right = None 
        self.val = data 
    
    def insert(self, newData): 
        if self.root is None: 
            self.root = Node(newData)
        else:
            self._insert(self.root, newData)
                
    def _insert(self, root, newData): 
        if newData > root.data: 
            root.left = Node(key)
        else:
            
        