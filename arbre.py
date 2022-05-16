

class Tree(object):
    
    from faker import Faker
    fake = Faker(locale="fr_FR")
    
    def __init__(self, value):

        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.next = None

    def add_node(self, value, client):
        
        new_node = Node(value, client)
        tmp_node = self
        tmp_tree = self
        new_node.client = client
        self.client = client
        
        while (tmp_tree != None):
            tmp_node = tmp_tree
            if (value < tmp_tree.value):
                tmp_tree = tmp_tree.left
                
                if (tmp_tree == None):
                    new_node.parent = tmp_node
                    tmp_node.left = new_node
                    
            elif (value > tmp_tree.value):
                tmp_tree = tmp_tree.right
                
                if (tmp_tree == None):
                    new_node.parent = tmp_node
                    tmp_node.right = new_node
                    
            elif (value == tmp_tree.value):
                
                while (tmp_node.next != None):
                    tmp_node = tmp_node.next
                
                tmp_node.next = new_node
                break

    def display_tree(self):
        
        if (self == None):
            return
        
        if (self.left != None):
            self.left.display_tree()
            
        print(f"* noeud n°{self.value}:\n")
        temp = self
        while (temp != None):
            print(f"  {temp.client.firstname}")
            print(f"  {temp.client.name}")
            print(f"  {temp.client.birth}")
            print(f"  {temp.client.email}")
            print(f"  {temp.client.hash}\n")
                
            temp = temp.next

        if (self.right != None):
            self.right.display_tree()
            
    

    def create_client(self):
        
        firstname = fake.first_name()
        name = fake.last_name()
        birth = fake.date_of_birth()
        email = fake.free_email()

        new_client = Client(firstname, name, birth, email)
        
        def hash(name):
                
            hash = len(name)
            for i in name:
                hash += ord(i)
            return hash % 100
        
        new_client.hash = hash(firstname+name)
        self.add_node(new_client.hash, new_client)
        print(name, hash(firstname+name))
        

class Node(Tree):

    def __init__(self, value, client):

        super().__init__(Tree)
        self.value = value
        self.client = client



class Client(object):

    def __init__(self, firstname, name, birth, email):

        self.firstname = firstname
        self.name = name
        self.birth = birth
        self.email = email
        self.next = None
        self.hash = None

if __name__ == "__main__":

    from faker import Faker
    fake = Faker(locale="fr_FR") 
    
    myTree = Tree(50)
    for i in range(500):
        myTree.create_client()
    
    print("\n")
    myTree.display_tree()
    
