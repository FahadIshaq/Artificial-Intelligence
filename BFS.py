class Node:
    # Init means initilizer and it is a constructor
    def __init__(self, state, parent, action):
        # double underscor means private
        # current object on which the method is called
        # state is the state of the node
        # self is the current object on which the method is called, it represents scope
        # parent is the parent of the node
        # action is the action that was taken to get to the node

        self.state = state
        self.parent = parent
        
        self.action = action


def actionSequence(graph, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent  # get the parent of the goal state
    while currentParent != None:  # if the frontier is empty and the goal state is not found
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def BFS():
    initialState = 'AE'
    goalState = 'Q'
    
    graph = {
    "A": Node('A', None, ["B"]),
    "B": Node('B', None, ["C"]),
    "C": Node('C', None, ["B","E","D"]),
    "D": Node('D', None, ["C","F","I"]),
    "E": Node('E', None, ["G","C",'F']),
    "F": Node('F', None, ["E","J", "D"]),
    "G": Node('G', None, ["E"]),
    "H": Node('H', None, ['I',"S"]),
    "I": Node('I', None, ['H',"J","D"]),
    "J": Node('J', None, ['I',"F","K"]),
    "K": Node('K', None, ['J',"L","T"]),
    "L": Node('L', None, ['K',"M"]),
    "M": Node('M', None, ['L',"N","U"]),
    "N": Node('N', None, ['O',"M"]),
    "O": Node('O', None, ['P',"N"]),
    "P": Node('P', None, ['O', "Q"]),
    "Q": Node('Q', None, ['P']),
    "R": Node('R', None, ['S']),
    "S": Node('S', None, ['R',"H"]),
    "T": Node('T', None, ['K',"X"]),
    "U": Node('U', None, ['V',"M","Y"]),
    "V": Node('V', None, ['U']),
    "W": Node('W', None, ['AA',"X"]),
    "X": Node('X', None, ['W',"T"]),
    "Y": Node('Y', None, ['U',"AC"]),
    "Z": Node('Z', None, ['AA',"AF"]),
    "AA": Node('AA', None, ['W','Z',"AG"]),
    "AB": Node('AB', None, ['AC']),
    "AC": Node('AC', None, ['AB',"Y","AD"]),
    "AD": Node('AD', None, ['AC',"AI"]),
    "AE": Node('AE', None, ['AF','AJ']),
    "AF": Node('AF', None, ['AE',"Z","AG"]),
    "AG": Node('AG', None, ['AF',"AA","AH"]),
    "AH": Node('AH', None, ['AG']),
    "AI": Node('AI', None, ['AD']),
    "AJ": Node('AJ', None, ['AE','AK']),
    "AK": Node('AK', None, ['AL','AJ']),
    "AL": Node('AL', None, ['R','AK'])
    
    
    
    
    }
    frontier = [initialState]  # Fifo Queue, Nodes to be explored
    explored = []  # List of explored nodes
    while len(frontier):
        currentNode = frontier.pop(0)
        explored.append(currentNode)
        for child in graph[currentNode].action:
            if child not in frontier and child not in explored:  # if child is not in frontier or explored
                # set the parent of the child to the current node
                graph[child].parent = currentNode
                if graph[child].state == goalState:  # if child is the goal state
                    return actionSequence(graph, goalState)
                frontier.append(child)  # Add to the end of the queue


print(BFS())
