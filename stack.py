#Author: Wyatt Avilla
#Date: 11/12/22
#File: Contains stack class
#implementation from https://runestone.academy/ns/books/published/pythonds/index.html

class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        return self.items.pop()

     def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
