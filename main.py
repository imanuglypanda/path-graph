import networkx as nx
import matplotlib.pyplot as plt

def wholeNumbers(size):
    for i in range(size):
        G.add_node(i)
        wholeNumbersNodes.append(i)

    
    for i in range(len(wholeNumbersNodes) - 1):
        wholeNumbersEdges.append([wholeNumbersNodes[i], wholeNumbersNodes[i + 1]])

    G.add_edges_from(wholeNumbersEdges, color='r')

    # print(wholeNumbersNodes)
    # print(wholeNumbersEdges)


def findOddAndEvenNumbers(size):
    number = 1
    while (len(oddNumbersNodes) < size or len(evenNumbersNodes) < size):
        if (number % 2 != 0):
            G.add_node(number)
            oddNumbersNodes.append(number)
        else:
            G.add_node(number)
            evenNumbersNodes.append(number)
        number += 1
        

def evenNumbers():
    for i in range(len(evenNumbersNodes) - 1):
        evenNumbersEdges.append([evenNumbersNodes[i], evenNumbersNodes[i + 1]])
    
    G.add_edges_from(evenNumbersEdges, color='g')

    # print(evenNumbersNodes)
    # print(evenNumbersEdges) 

def oddNumbers():
    for i in range(len(oddNumbersNodes) - 1):
        oddNumbersEdges.append([oddNumbersNodes[i], oddNumbersNodes[i + 1]])
    
    G.add_edges_from(oddNumbersEdges, color='b')

    # print(oddNumbersNodes)
    # print(oddNumbersEdges) 

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primesNumbers(size):
    number = 2
    while len(primesNumbersNodes) < size:
        if is_prime(number):
            G.add_node(number)
            primesNumbersNodes.append(number)
        number += 1

    for i in range(len(primesNumbersNodes) - 1):
        primesNumbersEdges.append([primesNumbersNodes[i], primesNumbersNodes[i + 1]])
    
    G.add_edges_from(primesNumbersEdges, color='y')

    # print(primesNumbersNodes)
    # print(primesNumbersEdges)

def fiveNodes(size):
    number = 5
    while(len(divisibleByFiveNodes) < size):
        G.add_node(number)
        divisibleByFiveNodes.append(number)
        number += 5
    
    for i in range(len(divisibleByFiveNodes) - 1):
        divisibleByFiveEdges.append([divisibleByFiveNodes[i], divisibleByFiveNodes[i + 1]])

    G.add_edges_from(divisibleByFiveEdges, color='m')

    # print(divisibleByFiveNodes)
    # print(divisibleByFiveEdges)

# Whole Number
wholeNumbersNodes = []
wholeNumbersEdges = []

# Even Number
evenNumbersNodes = []
evenNumbersEdges = []

# Odd Number
oddNumbersNodes = []
oddNumbersEdges = []

# Prime Number
primesNumbersNodes = []
primesNumbersEdges = []

# Divisible By Five
divisibleByFiveNodes = []
divisibleByFiveEdges = []

pathList = []

G = nx.MultiDiGraph()
size = 20

wholeNumbers(size) # Red
findOddAndEvenNumbers(size)
evenNumbers() # Green
oddNumbers() # Blue
primesNumbers(size) # Yellow
fiveNodes(size) # Magenta

colors = nx.get_edge_attributes(G, 'color').values()

pos = nx.kamada_kawai_layout(G)
nx.draw(
    G, 
    pos,
    with_labels=True,
    edge_color=colors, 
    node_color='lightgreen'
)
plt.show()