# NAME: FAHAD ISHAQ
# REG.NO: FA20-BCS-017
# LAB-03

# ---------------------------------------------- GRADED TASK 1----------------------------------------------------------

class Node:
    # Init means initilizer and it is a constructor
    def __init__(self, state, parent, action, cost):
        # double underscor means private
        # current object on which the method is called
        # state is the state of the node
        # self is the current object on which the method is called, it represents scope
        # parent is the parent of the node
        # action is the action that was taken to get to the node

        self.state = state
        self.parent = parent
        self.cost = cost
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
    initialState = 'Lugoj'
    goalstate = 'Oradea'

    graph = {
        'Oradea': Node('Oradea', None, ['Zerind', 'Sibiu'], None),
        'Zerind': Node('Zerind', None, ['Arad', 'Oradea'], None),
        'Arad': Node('Arad', None, ['Timisoara', 'Sibiu', 'Zerind'], None),
        'Timisoara': Node('Timisoara', None, ['Lugoj', 'Arad'], None),
        'Lugoj': Node('Lugoj', None, ['Mehadia', 'Timisoara'], None),
        "Mehadia": Node('Mehadia', None, ['Drobeta', 'Lugoj'], None),
        "Drobeta": Node('Drobeta', None, ['Craiova', 'Mehadia'], None),
        "Craiova": Node('Craiova', None, ['Rimnicu Vitcea', 'Pitesti', 'Drobeta'], None),
        "Rimnicu Vitcea": Node('Rimnicu Vitcea', None, ['Sibiu', 'Pitesti', 'Craiova'], None),
        "Pitesti": Node('Pitesti', None, ['Bucharest', 'Rimnicu Vitcea', 'Craiova'], None),
        "Sibiu": Node('Sibiu', None, ['Fagaras', 'Rimnicu Vitcea', 'Oradea'], None),
        "Fagaras": Node('Fagaras', None, ['Bucharest', 'Sibiu'], None),
        "Bucharest": Node('Bucharest', None, ['Giurgui', 'Urziceni', 'Fagaras', 'Pitesti'], None),
        "Giurgui": Node('Giurgui', None, ['Bucharest'], None),
        "Urziceni": Node('Urziceni', None, ['Hirsowa', 'Vaslui', 'Bucharest'], None),
        "Hirsowa": Node('Hirsowa', None, ['Eforic', 'Urziceni'], None),
        "Eforic": Node('Eforic', None, ['Hirsowa'], None),
        "Vaslui": Node('Vaslui', None, ['Iasi', 'Urziceni'], None),
        "Iasi": Node('Iasi', None, ['Neamt', 'Vaslui'], None),
        "Neamt": Node('Neamt', None, ['Iasi'], None)
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
                if graph[child].state == goalstate:  # if child is the goal state
                    return actionSequence(graph, goalstate)
                frontier.append(child)  # Add to the end of the queue


print(BFS())


# ---------------------------------------------- GRADED TASK 2----------------------------------------------------------
class Node:
    # Init means initilizer and it is a constructor
    def __init__(self, state, parent, action, cost):
        # double underscor means private
        # current object on which the method is called
        # state is the state of the node
        # self is the current object on which the method is called, it represents scope
        # parent is the parent of the node
        # action is the action that was taken to get to the node

        self.state = state
        self.parent = parent
        self.cost = cost
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
    initialState = 'A'
    goalstate = 'Z'
    graph = {
        'A': Node('A', None, ['B'], None),
        'B': Node('B', None, ['C'], None),
        'C': Node('C', None, ['D'], None),
        'D': Node('D', None, ['E', 'P'], None),
        'E': Node('E', None, ['F'], None),
        'F': Node('F', None, ['G'], None),
        'G': Node('G', None, ['H'], None),
        'H': Node('H', None, ['I'], None),
        'I': Node('I', None, ['J'], None),
        'J': Node('J', None, ['K'], None),
        'K': Node('K', None, ['L'], None),
        'L': Node('L', None, ['M'], None),
        'M': Node('M', None, ['P'], None),
        'N': Node('N', None, ['Q'], None),
        'O': Node('O', None, [], None),
        'P': Node('P', None, ['Q'], None),
        'Q': Node('Q', None, ['R', 'S'], None),
        'R': Node('R', None, ['T'], None),
        'S': Node('S', None, ['T'], None),
        'T': Node('T', None, ['U'], None),
        'U': Node('U', None, ['V'], None),
        'V': Node('V', None, ['W', 'X'], None),
        'W': Node('W', None, [], None),
        'X': Node('X', None, ['Y'], None),
        'Y': Node('Y', None, ['Z'], None),
        'Z': Node('Z', None, ['E'], None),
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
                if graph[child].state == goalstate:  # if child is the goal state
                    return actionSequence(graph, goalstate)
                frontier.append(child)  # Add to the end of the queue


print(BFS())
