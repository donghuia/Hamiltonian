import networkx as nx
import random
import numpy as np

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

'''
Defining our safe vertex as something which is not in our path
'''
def safeVertex(node):
    if (node in path):
        return False
    return True

'''
Defining our DFS and Backtracking Logic
'''
def cycleDetection(E, n, root):
    path.append(root)
    # Seeing all the neigbours of the current root
    for i in E[root]:
        # Checking if our vertex satisfies the safe Vertex
        if (safeVertex(i)):
            # Checking if a cycle has already been detected or not in the
            # ---------------------previous recursion--------------------
            if (cycleDetection(E, n, i)):
                return True

    # Checking if our current path has all the vertices
    if (len(path) == n):
        # If there is an edge from last vertex to the first vertex in our path
        # -------------then we have an hamiltonian cycle---------------------
        if (path[0] in E[path[len(path) - 1]]):
            return True
        else:
            return False
    # once we are done we remove that particle from the iteration
    path.pop()

'''
Printing True or False based on our output from Cycle Detection
'''
def HamiltonianCycle(E, n, root):
    if (cycleDetection(E, n, root)):
        return True
    else:
        return False

def matrix2table(martrix):
    result = []
    N = len(matrix)
    for i in range(N):
        tmp1 = []
        for j in range(N):
            if matrix[i][j]:
                tmp1.append(j)
        result.append(tmp1)
    return result

def table2matrix(table):
    ret = []
    N = len(table)
    for i in range(N):
        tmp = [0] * N
        for j in table[i]:
            tmp[j] = 1
        ret.append(tmp)
    return ret

if __name__ == "__main__":
    n = 2 
    k = 2
    f = 0
    G = constructGraph(n, k, 0)
    N = []
    for i in G.nodes:
        N.append(i)
    for i in G.edges:
        N.append(i)
    sum = 0
    PathLength = []
    length = 0
    for m in range(0, 1000):
        G1 = constructGraph(n, k, 0)
        Nodes = []
        for i in G1.nodes:
            Nodes.append(i)
        f = random.randrange(0, n*k-3+1)
        FaultyNodes = random.sample(N, f)
        print("Faulty Elements：", FaultyNodes)
        if len(FaultyNodes) != 0:
            for faulty in FaultyNodes:
                if faulty in Nodes:
                    G1.remove_node(str(faulty))
                    Nodes.remove(faulty)
                else:
                    faulty = str(faulty).replace("(", "")
                    faulty = str(faulty).replace(")", "")
                    N1 = faulty.split(', ')
                    N1[0] = N1[0].replace("'", "")
                    N1[1] = N1[1].replace("'", "")
                    if G1.has_edge(N1[0], N1[1]):
                        G1.remove_edge(N1[0], N1[1])
        path = []
        matrix = np.array(nx.adjacency_matrix(G1).todense())
        tb = matrix2table(matrix)
        flag = HamiltonianCycle(tb, len(Nodes), 0)
        # This path is actually a Hamiltonian cycle.
        print(path)
        if path:
            sum += 1
            print(len(path))
            PathLength.append(len(path))
            length += length + len(path)
print("The number of times to successfully find a Hamiltonian cycle is：",sum)
