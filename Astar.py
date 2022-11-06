import math

class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost): # Constructor
        self.state = state# State
        self.parent = parent# Parent
        self.actions = actions
        self.heuristic = heuristic
        self.totalCost = totalCost

def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier: # Loop through the frontier
        if minV > frontier[i][1]:# If the minimum value is greater than the frontier
            minV = frontier[i][1]# Set the minimum value to the frontier
            node = i
    return node # Astar function

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def Astar():
    initialState = 'A'
    goalState = 'Y'

    graph = {
        'A': Node('A', None, [('F',1)], (0,0),0),
        'B': Node('B', None, [('G',1), ('C',1)], (2,0),0),
        'C': Node('C', None, [('B',1), ('D',1)], (3,0),0),
        'D': Node('D', None, [('C',1), ('E',1)], (4,0),0),
        'E': Node('E', None, [('D',1)], (5,0),0),
        'F': Node('F', None, [('A',1), ('H',1)], (0,1),0),
        'G': Node('G', None, [('B',1), ('J',1)], (0,2),0),
        'H': Node('H', None, [('F',1), ('I',1), ('M',1)], (0,2),0),
        'I': Node('I', None, [('H',1), ('J',1), ('N',1)], (1,2),0),
        'J': Node('J', None, [('G',1), ('I',1)], (2,2),0),
        'K': Node('K', None, [('L',1), ('P',1)], (4,2),0),
        'L': Node('L', None, [('K',1), ('Q',1)], (5,2),0),
        'M': Node('M', None, [('H',1), ('N',1), ('R',1)], (0,3),0),
        'N': Node('N', None, [('I',1), ('M',1), ('S',1)], (1,3),0),
        'O': Node('O', None, [('P',1), ('U',1)], (3,3),0),
        'P': Node('P', None, [('O',1), ('Q',1)], (4,3),0),
        'Q': Node('Q', None, [('L',1), ('P',1), ('V',1)], (5,3),0),
        'R': Node('R', None, [('M',1), ('S',1)], (0,4),0),
        'S': Node('S', None, [('N',1), ('R',1), ('T',1)], (1,4),0),
        'T': Node('T', None, [('S',1), ('U',1), ('W',1)], (2,4),0),
        'U': Node('U', None, [('O',1), ('T',1)], (3,4),0),
        'V': Node('V', None, [('Q',1), ('Y',1)], (5,4),0),
        'W': Node('W', None, [('T',1)], (2,5),0),
        'X': Node('X', None, [('Y',1)], (4,5),0),
        'Y': Node('Y', None, [('V',1), ('X',1)], (5,5),0),
    }

    frontier = dict()
    heuristicCost = math.sqrt(((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])**2) + ((graph[goalState].heuristic[1] - graph[initialState].heuristic[1])**2)) # Heuristic cost function using the Euclidean distance formula to calculate the distance between the goal state and the initial state
    frontier[initialState] = (None, heuristicCost) # Add the initial state to the frontier with the heuristic cost as the value of the key in the dictionary 
    explored = dict() # Explored dictionary to store the explored nodes in the graph and their respective costs 

    while len(frontier)!= 0:
        currentNode = findMin(frontier)
        print("Current Node: ",currentNode) # Print the current node
        del frontier[currentNode] # Delete the current node
        if graph[currentNode].state == goalState: # If the current node is the goal state
            return actionSequence(graph,initialState,goalState) # Return the action sequence
        
        heuristicCost = math.sqrt(((graph[goalState].heuristic[0]-graph[currentNode].heuristic[0])**2)+((graph[goalState].heuristic[1]-graph[currentNode].heuristic[1])**2)) # Calculate the heuristic cost
        currentCost = graph [currentNode].totalCost # Set the current cost to the total cost
        explored[currentNode]=(graph[currentNode].parent, heuristicCost+currentCost) # Add the current node to the explored list
        for child in graph[currentNode].actions: # Loop through the actions
            currentCost = child[1] + graph[currentNode].totalCost # Set the current cost to the child cost plus the total cost
            heuristicCost = math.sqrt(((graph[goalState].heuristic[0]-graph[child[0]].heuristic[0])**2)+((graph[goalState].heuristic[1]-graph[child[0]].heuristic[1])**2))
            if child[0] in explored: # If the child is in the explored list
                if graph[child[0]].parent == currentNode or child[0]==initialState or explored[child[0]][1]<=currentCost+heuristicCost: # If the parent is the current node or the child is the initial state or the explored cost is less than or equal to the current cost plus the heuristic cost
                    continue # Continue
            if child[0] not in frontier: # If the child is not in the frontier
                graph[child[0]].parent=currentNode # Set the parent to the current node
                graph[child[0]].totalCost=currentCost # Set the total cost to the current cost
                frontier[child[0]]= (graph[child[0]].parent, currentCost+heuristicCost) # Add the child to the frontier
            else: # Else if child is in the frontier
                if frontier[child[0]][1] < currentCost + heuristicCost: # If the frontier cost is less than the current cost plus the heuristic cost
                    graph[child[0]].parent=frontier[child[0]][0] # Set the parent to the frontier parent
                    graph[child[0]].totalCost=frontier[child[0]][1] - heuristicCost # Set the total cost to the frontier cost minus the heuristic cost
                else:# Else if the frontier cost is greater than the current cost plus the heuristic cost
                    frontier[child[0]]= (currentNode, currentCost + heuristicCost) # Set the frontier to the current node and the current cost plus the heuristic cost
                    graph[child[0]].parent=frontier[child[0]][0] # Set the parent to the frontier parent
                    graph[child[0]].totalCost=currentCost # Set the total cost to the current cost

solution = Astar()
print("Solution: ",solution)
