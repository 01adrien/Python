from random import randint


class Stack(object):

    def __init__(self):

        self.first = None
        self.length = 0

    def pop(self):

        self.first.value = 0
        self.first = self.first.next
        self.length -= 1

    def add(self, value):

        new_node = Node(value, self.first)
        self.first = new_node
        self.length += 1

    def display(self):
        
        temp = self.first
        print("[", end="")
        while temp.next != None:
            print(f"'{temp.value}'", end=", ")
            temp = temp.next
        print(f"'{temp.value}']")
    
    def len(self):

        return self.length

    def max_min(self):

        temp = self.first
        maxi = self.first.value
        mini = self.first.value
        
        while temp != None:
            if temp.value < mini:
                mini = temp.value
            elif temp.value > maxi:
                maxi = temp.value
            temp = temp.next

        return (maxi, mini)
    
        
class Node(object):

    def __init__(self, value, next):

        self.value = value
        self.next = next



if __name__ == "__main__":

    from random import randint

    myStack = Stack()
    print(f"len = {myStack.len()}")
    for i in range(1,8):
        myStack.add(i*3)
    myStack.display()
    print(myStack.max_min())
    print(f"len = {myStack.len()}")
    myStack.pop()
    myStack.display()
    print(f"len = {myStack.len()}")
    
    

    
