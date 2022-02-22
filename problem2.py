## Problem 2:(https://leetcode.com/problems/design-hashset/)


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"key:{self.key}"

class MyHashSet:

    def __init__(self):
        self.max_size = 10000                           #Initialized the maximum size
        self.arr = [None for i in range(self.max_size)] # Array of size max_szie all element none
        

    def add(self, key: int) -> None:
        node = Node(key)                                #Define a new node object
        
        if self.arr[ key % self.max_size  ] is None:    # if the position is none
            self.arr[ key % self.max_size  ] = node     # add the new node there and return
            return
        
        temp = self.arr[ key % self.max_size ]          #find the first node at the position
        
        while temp:                                     #loop through all the nodes in LL
            if temp.key == key:                         #if key already present 
                return
            if temp.next is None:                       #if this is the last node
                break                                   #break out of the loop
            temp = temp.next                            
            
        temp.next = node                                #attach the node in the last position
        return
        

    def remove(self, key: int) -> None:
        if self.arr[ key % self.max_size  ] is None:
            return
        prev = None                                     #prev node points to None
        temp = self.arr[ key % self.max_size ]          # first node of LL
        
        while temp:                                     #Loop through all the nodes
            if temp.key == key:
                
                if prev == None:                        #if its the first node
                    self.arr[ key % self.max_size ] = temp.next #Point to the node after first node
                else:
                    prev.next = temp.next               # pre.next points to temp.next
                del temp
                return
            prev = temp                                 #update prev and temp
            temp = temp.next
        
        

    def contains(self, key: int) -> bool:
        temp = self.arr[ key % self.max_size ]          #first node of the position
        
        while temp:                                     #Loop over all the elements
            if temp.key == key:                         #if the node's key == key
                return True                             #return True
            temp = temp.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)