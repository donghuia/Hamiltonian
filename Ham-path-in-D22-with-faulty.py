import networkx as nx
import random

def constructGraph(n,k,I):
    f1=n*1+1
    f2=n*f1+1
    G = nx.Graph() 
    for x1 in range(0,f1):
        for x2 in range(0,f2):
            G.add_node(str(x2)+','+str(x1))
    for i in range(0,f2):
        for j in range(0,f1):
            for l in range(j+1,f1):
                G.add_edge(str(i)+','+str(j), str(i)+','+str(l), weight=1)
    for node in G.nodes:
        node = node.split(',')
        x2=int(node[0])
        x1=int(node[1])
        y1=f1-1-x1
        y2_list=[]
        for j in range(1,n+1):
            y2_list.append((n*x1+x2+j)%f2)
        for y2 in y2_list:
            G.add_edge(str(x2) + ',' + str(x1), str(y2) + ',' + str(y1))
    return G

def dfs(graph, visited, start, end):
    visited.append(start)
    if start == end and len(visited) == len(graph):
        return visited
    for next_node in graph[start]:
        if next_node not in visited:
            path = dfs(graph, visited, next_node, end)
            if path:
                return path
    visited.pop()

def hamiltonian_path(graph,start,end):
    visited = []
    path = dfs(graph, visited, start, end)
    if path:
        return path
    else:
        return 1

n=2 
k=2
G=constructGraph(n,k,0)
N = []
Nodes = []
Edges = []
for i in G.nodes:
    N.append(i)
    Nodes.append(i)
for i in G.edges:
    N.append(i)
    Edges.append(i)
sum = 0
for start in Nodes:
    for end in Nodes:
        if start!=end:
            G1 = constructGraph(n,k,0)
            FaultyNumber = random.randrange(0, n*k-3+1)
            print("Number of faults=", FaultyNumber)
            print("Start Node：",start)
            print("End Node：",end)
            ST = [start,end]
            F = [x for x in N if x not in ST]
            FaultySet = random.sample(F, FaultyNumber)
            print("Faulty Element Set：",FaultySet)
            for faulty in FaultySet:
                if faulty in Nodes:
                    G1.remove_node(str(faulty))
                if faulty in Edges:
                    print(faulty)
                    faulty = str(faulty).replace("(","")
                    faulty = str(faulty).replace(")", "")
                    print(faulty)
                    N1=faulty.split(', ')
                    N1[0]=N1[0].replace("'", "")
                    N1[1] = N1[1].replace("'", "")
                    G1.remove_edge(N1[0],N1[1])
            print(len(G1))
            path=hamiltonian_path(G1,start,end)
            if path==1:
                sum+=1
            print(path)
print("The number of times that the Hamiltonian path cannot be found is：",sum)
