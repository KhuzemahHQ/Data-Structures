class Edge:
    def __init__(self, origin, dest, weight):
       self.origin = origin
       self.dest = dest
       self.weight = weight

class Graph:
    def __init__(self, filename, flag):
        """
        Graph constructor
        You will implement your graph here either using adjacency list or adjacency matrix
        True flag -> directed graph, False flag -> undirected graph 
        filename will be the .txt file from which you will be loading your graph
        Format of .txt file is as given in the manual
        Construct this class as you deem fit 
        """
        # It is known that the road connectivity is low
        # I will be using an adjacency list as they have better time complexity and memory footprint in sparse graphs with O(|V|+|E|) compared to O(|V|^2) of adjacency matrix

        file = open(filename, 'r')
        lines = file.readlines()
        # self.V = int(lines[0][2:])
        # self.E = int(lines[1][2:])

        self.graph = {}
        vertex_list = []
        # Sorting vertexes alphabetically
        for i in range(2,len(lines)):
            if lines[i][0] not in vertex_list:
                vertex_list.append(lines[i][0])
            if lines[i][2] not in vertex_list:
                vertex_list.append(lines[i][2])
        vertex_list = sorted(vertex_list)

        self.V = vertex_list
        self.E = []

        # Creating dictionary in alphabetical order
        for vertex in vertex_list:
            self.graph[vertex] = []

        # Adding edges
        for i in range(2,len(lines)):
            start = lines[i][0]
            end = lines[i][2]
            weight = int(lines[i][4:])
            self.add_edge(start,end,weight,flag)
        
        # Sorting edges by destination alphabetically
        for edge_list in self.graph.values():
            edge_list = self.sort_edges_by_dest(edge_list)
    
    def add_edge(self, start, end, weight, flag):
        """
        inserts edge connecting start and end with weight to the graph
        does not require a return value 
        """
        node = Edge(start,end,weight)
        self.graph[start].append(node)
        self.E.append(node)

        if flag == False:
            node = Edge(end,start,weight)
            self.graph[end].append(node)
            self.E.append(node)

    # Helper Function to sort edges by destination
    def sort_edges_by_dest(self,edge_list):
        for i in range(len(edge_list)):
            for j in range(i,len(edge_list)):
                if edge_list[j].dest <edge_list[i].dest:
                    temp = edge_list[i]
                    edge_list[i] = edge_list[j]
                    edge_list[j] = temp

        return edge_list
    
    def display(self):
        """
        displays the graph in a certain format (given in Manual)
        returns a string 
        """
        result = ""
        for edge_list in self.graph.values():
            for element in edge_list:
                x = "(" + str(element.origin) +","+str(element.dest)+","+str(element.weight)+")" 
                result = result +" "+ x
        # To remove initial space in string
        result = result[1:]
        return result


    def reachable(self, start, end):
        """
        determines if node end is reachable by node start
        returns a boolean
        """
        # Doing Breadth First Search
        # Making list of all nodes reachable from start
        discovered = []
        level = [start]
        while len(level) > 0:
            next_level = []
            for node in level:
                edge_list = self.graph[node]
                for edge in edge_list:
                    if edge.dest not in discovered:
                        discovered.append(edge.dest)
                        next_level.append(edge.dest)
            level = next_level
        if end in discovered:
            return True
        else:
            return False


    def dijkstra(self, start, end):
        """
        determines shortest path between start and end
        returns an int
        """
        if self.reachable(start,end) == False:
            return -1

        unvisited = []
        for vertex in self.V:
            unvisited.append(vertex)

        shortest_distance = {}
        for node in unvisited:
            shortest_distance[node] = float('inf')
        shortest_distance[start] = 0

        while len(unvisited) > 0:
            current_min = None
            # finding closest unvisited node with smallest weight
            for node in unvisited:
                if current_min is None:
                    current_min = node
                elif shortest_distance[node] < shortest_distance[current_min]:
                    current_min = node

            adjacent = self.graph[current_min]
            for next in adjacent:
                temp = shortest_distance[current_min]+next.weight
                if temp < shortest_distance[next.dest]:
                    shortest_distance[next.dest] = temp
            
            unvisited.remove(current_min)

        return shortest_distance[end]


    # Helper Function for visiting all unvisited nodes and appending to result list
    def recursive_topo(self,vertex,visit,result):
        visit[vertex] = True

        for edge in self.graph[vertex]:
            if visit[edge.dest] == False:
                self.recursive_topo(edge.dest,visit,result)

        result.append(vertex)
        
    
    def topo_sort(self):
        """
        sorts the graph using the toposort algorithm
        returns a string. Format: ABCDEF
        """
        visit = {}
        for vertex in self.V:
            visit[vertex] = False
        result = []
        
        for i in self.V:
            if visit[i] == False:
                self.recursive_topo(i,visit,result)
        result.reverse()
        string = ""
        for node in result:
            string += node
        return string
        
            
def main():
    # You can make your own graph to test here
    pass

# main()