import networkx as nx
import matplotlib.pyplot as plt

def wholeNumbers(size):
    for i in range(size):
        wholeNumbersList.append(i)

    for i in range(size - 1):
        G.add_edge(
            wholeNumbersList[i],
            wholeNumbersList[i + 1],
            color = 'r'
        )
        

def evenNumbers(size):
    count = 0
    G.add_edge(2, 4)
    count += 1
    even = 4
    while(count < size - 1):
        G.add_edge(
            even, 
            even + 2, 
            color='g'
        )
        even += 2
        count += 1
        

def oddNumbers(size):
    count = 0
    G.add_edge(1, 3)
    count += 1
    odd = 3
    while(count < size - 1):
        G.add_edge(
            odd, 
            odd + 2, 
            color='b'
        )
        odd += 2
        count += 1

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primesNumbers(size):
    primes = []
    number = 2
    while len(primes) < size:
        if is_prime(number):
            primes.append(number)
        number += 1
    for i in range(len(primes)):
        if (i == len(primes) - 1):
            break
        else:
            G.add_edge(
                primes[i], 
                primes[i + 1],
                color='y'
            )

def fiveNodes(size):
    number = 5
    for i in range(size):
        if (i > 0):
            G.add_edge(
                number - 5,
                number,
                color='m'
            )
        number += 5

wholeNumbersList = []
evenNumbersList = []
oddNumbersList = []
primesNumbersList = []
fiveNodesList = []
graphNumbersList = []

G = nx.DiGraph(Directed=True)
size = 20

wholeNumbers(size) # Red
# evenNumbers(size) # Green
# oddNumbers(size) # Blue
# primesNumbers(size) # Yellow
# fiveNodes(size) # Magenta

colors = nx.get_edge_attributes(G,'color').values()

pos = nx.kamada_kawai_layout(G)
nx.draw(
    G, 
    pos,
    edge_color=colors, 
    with_labels=True,
    node_color='lightgreen'
)
plt.show()