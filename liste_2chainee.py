class Liste(object):

    def __init__(self):

        self.length = 0
        self.first = None
        self.end = None

    def add(self, value):

        new_node = Node(value)

        if (self.end == None):
            self.end = new_node
            new_node.next = None
            

        elif (self.first == None):
            self.first = new_node
            self.end.last = self.first
            new_node.next = self.end
            new_node.last = None

        else:
            self.first.last = new_node
            new_node.next = self.first
            new_node.last = None
            self.first = new_node
            
        self.length +=1

    def one(self, n):

        node = self.first
        for i in range(n):
            node = node.next

        return node

        
    def display(self, side):

        if (side == "G"):
            node = self.first
            while (node != None):
                print(f"{node.value}", end=" ")
                node = node.next

        elif (side == "D"):
            node = self.end
            while (node != None):
                print(f"{node.value}", end=" ")
                node = node.last
        print("\n")

    def pop(self, n):

        node = self.one(n)
        last = node.last
        next = node.next
        last.next = next
        next.last = last
        node.value = 0

class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None
        self.last = None


if __name__ == "__main__":

    maListe = Liste()
    for i in range(10):
        maListe.add(i+1*3)
    maListe.display("G")
    maListe.pop(6)
    maListe.display("G")
    
