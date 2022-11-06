import math


class Node:
    #state = state
    # __ means that the scope of the method is private
    def __init__(self,state,parent,actions,totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

# def actionSequence(graph, goalState):
# pass
def actionSequence(graph,initialState,goalState):
    #returns the list of states starting from goal state moving upwards
    # towards parent unitl root is reached
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def findMin(frontier):
    #returns that node in the frontier which has a lowest cost
    minV = math.inf
    node=''
    for i in frontier:
        if minV > frontier[i][1]:
            minV=frontier[i][1]
            node = i
    
    return node
def UCS():
    initialState = 'AE'
    goalState = 'Q'

    graph = {
    "A": Node('A', None, [("B",1)],0),
    "B": Node('B', None, [("C",1)],0),
    "C": Node('C', None, [("B",1),("E",1),("D",1)],0),
    "D": Node('D', None, [("C",1),("F",1),("I",1)],0),
    "E": Node('E', None, [("G",1),("C",1),('F',1)],0),
    "F": Node('F', None, [("E",1),("J",1), ("D",1)],0),
    "G": Node('G', None, [("E",1)],0),
    "H": Node('H', None, [('I',1),("S",1)],0),
    "I": Node('I', None, [('H',1),("J",1),("D",1)],0),
    "J": Node('J', None, [('I',1),("F",1),("K",1)],0),
    "K": Node('K', None, [('J',1),("L",1),("T",1)],0),
    "L": Node('L', None, [('K',1),("M",1)],0),
    "M": Node('M', None, [('L',1),("N",1),("U",1)],0),
    "N": Node('N', None, [('O',1),("M",1)],0),
    "O": Node('O', None, [('P',1),("N",1)],0),
    "P": Node('P', None, [('O',1), ("Q",1)],0),
    "Q": Node('Q', None, [('P',1)],0),
    "R": Node('R', None, [('S',1)],0),
    "S": Node('S', None, [('R',1),("H",1)],0),
    "T": Node('T', None, [('K',1),("X",1)],0),
    "U": Node('U', None, [('V',1),("M",1),("Y",1)],0),
    "V": Node('V', None, [('U',1)],0),
    "W": Node('W', None, [('AA',1),("X",1)],0),
    "X": Node('X', None, [('W',1),("T",1)],0),
    "Y": Node('Y', None, [('U',1),("AC",1)],0),
    "Z": Node('Z', None, [('AA',1),("AF",1)],0),
    "AA": Node('AA', None, [('W',1),('Z',1),("AG",1)],0),
    "AB": Node('AB', None, [('AC',1)],0),
    "AC": Node('AC', None, [('AB',1),("Y",1),("AD",1)],0),
    "AD": Node('AD', None, [('AC',1),("AI",1)],0),
    "AE": Node('AE', None, [('AF',1),('AJ',1)],0),
    "AF": Node('AF', None, [('AE',1),("Z",1),("AG",1)],0),
    "AG": Node('AG', None, [('AF',1),("AA",1),("AH",1)],0),
    "AH": Node('AH', None, [('AG',1)],0),
    "AI": Node('AI', None, [('AD',1)],0),
    "AJ": Node('AJ', None, [('AE',1),('AK',1)],0),
    "AK": Node('AK', None, [('AL',1),('AJ',1)],0),
    "AL": Node('AL', None, [('R',1),('AK',1)],0)
    
    }
    frontier = dict()
    frontier[initialState] = (None,0) # parent of initian node is none os its cost is 0
    explored = []

    while len(frontier)!=0:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            
            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent,graph[child[0]].totalCost)
            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
                else:
                    frontier[child[0]] =(currentNode,currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]
    print(graph[initialState].totalCost)
    

solution = UCS()
print(solution)