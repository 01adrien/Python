class Liste(object):

    def __init__(self):

        self.first = None
        self.length = 0

    def add_node(self, value):

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

        
    def index(self, n):

        temp = self.first
        for i in range(n-1):
            temp = temp.next
    
        return temp

    def add_someone(self, job, name, tel, city):
        
        new_one = Person(job, name, tel, city)
        node = self.index(self.hash(name))
        if node.first_one == None:
            node.first_one = new_one
            new_one.next = None

        else:
            new_one.next = node.first_one
            node.first_one = new_one

    def hash(self, name):

        hash = len(name)
        for i in name:
            hash += ord(i)

        return hash % self.length

    def display_box(self, n):

        s = "-"*35
        node = self.index(n)
        p = node.first_one
        print(f"{s} Hash {n} {s}\n")
        while p != None:
            print(f"{p.name}\n{p.city}\n{p.tel}\n{p.job}\n")
            p = p.next

    def display_all_boxs(self):

        for i in range(self.length):
            self.display_box(i)

    def find (self, name):

        node = self.index(self.hash(name))
        node = node.first_one
        while node.name != name:
            node = node.next
            if node == None:
                break
        if node:
            print(f"trouvé dans le box {self.hash(name)}")
            print(f"{node.name}\n{node.tel}\n{node.city}\n{node.job}")

        else:
            print(f"Pesonne au nom de {name}")
            
            
class Node(object):

    def __init__(self, value, next):

        self.first_one = None
        self.value = value
        self.next = next
        
            
class Person(object):

    def __init__(self, job, name, tel, city):

        self.job = job
        self.name = name
        self.tel = tel
        self.city = city
        self.next = None
    

if __name__ == "__main__":

    from faker import Faker
    fake = Faker(locale='fr_FR')

    hashList = Liste()
    for i in range(40):
        hashList.add_node(i)
    for i in range(500):
        name = fake.first_name()
        tel = fake.phone_number()
        city = fake.city()
        job = fake.job()
        hashList.add_someone(job, name, tel, city)
    #hashList.display_all_boxs()
    hashList.find("Luce")
