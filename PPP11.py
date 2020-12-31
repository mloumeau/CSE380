from graph_test_dict import graph_test_dict

def getEdgeListFromFile(fileName):
    edgeList = []
    try:
        file = open(fileName)
        
        for x in file:
            edgeList.append(tuple(map(int, x.split(" "))))

        file.close()
    except:
        print("ERROR: Issue reading file named", fileName)
        return None
    return edgeList

def buildGraphFromEdges(edgeList):
    graph = [[], []]
    for x in edgeList:
        if not (x[0] in graph[0]):
            graph[0].append(x[0])
        if not (x[1] in graph[0]):
            graph[0].append(x[1])
        graph[1].append(x)

    return graph

def getGraphFromFile(fileName):
    edgeList = getEdgeListFromFile(fileName)

    if edgeList == None:
        return None
    return buildGraphFromEdges(edgeList)

def get_adjacency_list(graph):
    adjList = {}

    for x in graph[0]:
        adjList[x] = []
    
    for x in graph[1]:
        adjList[x[0]].append(x[1])
        adjList[x[1]].append(x[0])

    return adjList

def link_exists(adjList, node1, node2):
    return (node1 in adjList[node2]) or (node2 in adjList[node1])


def check_clique_or_anti_clique(graph, adjList, nodes, anti):
    for x in range(0, len(nodes) - 1):
        for y in range(x + 1, len(nodes)):
            if link_exists(adjList, nodes[x], nodes[y]) == anti:
                return False
    return True

def testFunctions(graph, adjList, nodes):
    print(check_clique_or_anti_clique(graph, adjList, nodes, False), check_clique_or_anti_clique(graph, adjList, nodes, True))


graphs=[]
adjList=[]
for i in range(6):
    graphs.append(getGraphFromFile(f"graph{i+1}.in"))
    adjList.append(get_adjacency_list(graphs[i]))
    print(f"GRAPH {i+1}:")
    for y in range(4):
        testFunctions(graphs[i], adjList[i], graph_test_dict[i+1][y])
