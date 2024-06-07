import networkx as nx

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
        return "No hamiltonian path exists"

n=2
k=2
G=constructGraph(n,k,0)
N = []
for i in G.nodes:
    N.append(i)
for start in N:
    for end in N:
        if start!=end:
            path=hamiltonian_path(G,start,end)
            print(path)
