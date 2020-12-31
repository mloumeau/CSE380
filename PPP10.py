import random

graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'C'],
         'C': ['A', 'B', 'E'],
         'D': ['A', 'F'],
         'E': ['F', 'C'],
         'F': ['D', 'E']}

ladderGraph = {'A': ['B', 'C'],
               'B': ['A', 'D'],
               'C': ['A', 'D', 'E'],
               'D': ['B', 'C', 'F'],
               'E': ['C', 'F'],
               'F': ['D', 'E']}

bullGraph = {'A': ['B'],
             'B': ['C', 'D'],
             'C': ['B', 'D'],
             'D': ['B', 'C', 'E'],
             'E': ['D']}


def getNodes(graphChoice):
    nodes = list(graphChoice.keys())
    return nodes

def getUnvisited(nodes):
    return nodes[1:]

def getVisited(nodes):
    return [nodes[0]]

def createPotential():
    for node in visited:
                        #Remove hardcode
        for adjacency in bullGraph[node]:
            if adjacency in unvisited:
                return (node, adjacency)
    return 0

def createSpanningTree(keyword):
    potential = createPotential()   
    if not potential:
        return
    
    visited.append(potential[1])
    unvisited.remove(potential[1]) 
    return potential


nodesBull = getNodes(bullGraph)
unvisited = getUnvisited(nodesBull)

random.shuffle(nodesBull)

visited = getVisited(nodesBull)

answer1 = list(map(createSpanningTree, nodesBull))
answer1 = [x for x in answer1 if x != None]

# nodes =  getNodes(graph)
# unvisited = getUnvisited(nodes)

# random.shuffle(nodes)

# visited = getVisited(nodes)

# answer2 = list(map(createSpanningTree, nodes))
# answer2[:] = [x for x in answer2 if x != None]

# nodesLadder = getNodes(ladderGraph)
# unvisited = getUnvisited(nodesLadder)

# random.shuffle(nodesLadder)

# visited = getVisited(nodesLadder)

# answer3 = list(map(createSpanningTree, nodesLadder))
# answer3[:] = [x for x in answer3 if x != None]

print(answer1)
# print(answer2)
# print(answer3)
