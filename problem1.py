## Problem 1: (https://leetcode.com/problems/implement-queue-using-stacks/)

class MyQueue:

    def __init__(self):
        self.stack1 = []                                # initilize stack1 and stack2
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)                           #add the number to stack1
        

    def pop(self) -> int:
        
        while len(self.stack1) != 0:                    #keep popping from stack 1 and add to stack2
            self.stack2.append( self.stack1.pop() )
            
        val = self.stack2.pop()                         #pop from stack2
        
        while len(self.stack2) != 0:                    #keep popping from stack 2 and add to stack1
            self.stack1.append( self.stack2.pop() )
            
        return val                                      #return the value

    def peek(self) -> int:
        if not self.empty():                            #return the first element of stack1
            return self.stack1[0]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()