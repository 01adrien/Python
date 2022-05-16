import os
from faker import Faker

class Graph(object):
    
    def __init__(self, nbr_vertices, vertices_names, is_oriented = False):

        self.fake = Faker(locale="fr_FR")
        self.vertices_names = vertices_names
        self.is_oriented = is_oriented
        self.nbr_vertices = nbr_vertices
        self.adjency_list = list()
        self.graphvizlist = list()
        
        for i in range(len(self.nbr_vertices)):
            self.adjency_list.append([nbr_vertices[i]])
            self.adjency_list[i].append([])
            
            self.graphvizlist.append([nbr_vertices[i]])
            self.graphvizlist[i].append([])

    def add_edge(self, src, dst, weight):

        if self.is_oriented == False:
            self.adjency_list[src][1].append((self.vertices_names[dst], weight))
            self.adjency_list[dst][1].append((self.vertices_names[src], weight))

        else:
            self.adjency_list[src][1].append((dst, weight))

        self.graphvizlist[src][1].append((dst, weight))

    def show_adjency_list(self):

        for i in self.adjency_list:
            print(f"vertice {self.vertices_names[i[0]]} -> {i[1]}")

    def algo_dijkstra(self):

        self.shortest_path = [0] * len(self.adjency_list)
        self.shortest_path[1] = 0        
        self.previous = [None] * len(self.adjency_list)
        self.previous[1] = 0
        
        for i in range(len(self.shortest_path)):
            print(f"\nprevious{self.previous}")
            print(f"shortest{self.shortest_path}\n")
            for j in self.adjency_list[i][1]:
                #print(j[0])
                print(f"\nprevious{self.previous}")
                print(f"shortest{self.shortest_path}\n")
                #print(f"{j[0]} == {s}")
                next_vertice = self.vertices_names.index(j[0])
                
                if self.previous[next_vertice] is None:    
                    self.shortest_path[next_vertice] = j[1] + self.shortest_path[self.adjency_list[i][0]]
                    self.previous[next_vertice] = self.vertices_names[self.adjency_list[i][0]]
                    
                elif self.previous[next_vertice]:
                    if j[1] + self.shortest_path[self.adjency_list[i][0]] < self.shortest_path[next_vertice]:
                        self.shortest_path[next_vertice] = j[1] + self.shortest_path[self.adjency_list[i][0]]
                        self.previous[next_vertice] = self.vertices_names[self.adjency_list[i][0]]
                        
                            
        print(f"\nprevious{self.previous}")
        print(f"shortest{self.shortest_path}\n")

    def draw_graph(self):

        with open("test.dot", "w") as g:
            
            if self.is_oriented == False:
                g.write("graph G {\n\n")
                for i in self.graphvizlist:
                    g.write(f"  {i[0]} [label=\"{self.vertices_names[i[0]]}\"];\n")
                    for j in i[1]:
                        g.write(f"  {i[0]} -- {j[0]} [label=\"{j[1]}\"];\n")
                g.write("\n}")

            else:
                g.write("digraph G {\n\n")
                g.write(f"{i[0]} [label=\"{self.vertices_names[i[0]]}\"];\nx")
                for i in self.graphvizlist:
                    for j in i[1]:
                        g.write(f"  {i[0]} -> {j[0]} [label=\"{j[1]}\"];\n")
                g.write("\n}")
        

    def show_graph(self, circle = True):

        self.draw_graph()
        if circle == True:
            os.system("circo -Tpng test.dot -o test.png && xdg-open test.png")

        else:
            os.system("dot -Tpng test.dot -o test.png && xdg-open test.png")


    def swap(self):

        self.adjency_list.append(self.adjency_list[0])
        self.adjency_list.pop(0)
        
        #self.vertices_names.append(self.vertices_names[0])
        #self.vertices_names.pop(0)
        print(self.vertices_names)
        print(self.adjency_list)
        self.show_adjency_list()
            
if __name__ == "__main__":

    vertices_names = ["A", "B", "C", "D", "E", "F"]
    vertices_num = [0, 1, 2, 3, 4, 5]
    new_graph = Graph(vertices_num, vertices_names)
    new_graph.add_edge(0, 1, 8)
    new_graph.add_edge(0, 2, 15)
    new_graph.add_edge(0, 4, 20)
    new_graph.add_edge(0, 5, 3)
    new_graph.add_edge(1, 2, 2)
    new_graph.add_edge(1, 3, 22)
    new_graph.add_edge(1, 4, 30)
    new_graph.add_edge(3, 2, 18)
    new_graph.add_edge(3, 5, 4)
    new_graph.add_edge(3, 4, 8)
    new_graph.add_edge(5, 4, 15)
    new_graph.swap()
    new_graph.algo_dijkstra()
    new_graph.show_adjency_list()
    for i in new_graph.adjency_list:
        print(i)
    new_graph.show_graph()
    
    
