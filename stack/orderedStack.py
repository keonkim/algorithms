#The stack remains always ordered such that the highest value is at the top and the lowest at the bottom

class Stack:
     def __init__(self):
         self.items = []
         
     def isEmpty(self):
         return self.items == []
         
     def pushT(self, item):
         self.items.append(item)
	     
     def push(self, item): #push method to maintain order when pushing new elements
         temp=Stack()
         if self.isEmpty() or item>self.peek():
             self.pushT(item)
         else:
             while (item<self.peek()) and (not self.isEmpty()):
                 temp.pushT(self.pop())
             self.pushT(item)
             while not(temp.isEmpty()):
                 self.pushT(temp.pop())
	 		    
     def pop(self):
         if self.isEmpty():
             raise IndexError("Stack is empty")
         return self.items.pop()
         
     def peek(self):
         return self.items[len(self.items)-1]
         
     def size(self):
         return len(self.items)
         
     def printStack(self):
	     sz=self.size()
	     for i in range(0, sz):
	 	    print(self.items[sz-i-1])

#MAIN
s=Stack()
s.push(1)
s.push(12)
s.push(8)
s.push(3)
s.pop()
s.printStack()
