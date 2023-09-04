import networkx as nx
import matplotlib.pyplot as plt

def wholeNumbers(size):
    for i in range(size):
        if (i < size):
            G.add_node(i)
            if (i > 0):
                G.add_edge(
                    i - 1, 
                    i, 
                    color='r', 
                    weight = 1
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
            color='g', 
            weight = 1
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
            color='b', 
            weight = 1
        )
        odd += 2
        count += 1

def oddEvenNumbers(size):
    oddNumbers = []
    evenNumbers = []
    numbers = 0
    oddNumbers.append(numbers)
    evenNumbers.append(numbers)
    numbers += 1
    
    while (len(oddNumbers) < size or len(evenNumbers) < size):
        if (numbers % 2 == 0):
            evenNumbers.append(numbers)
        else:
            oddNumbers.append(numbers)
        numbers += 1
    for i in range(size):
        
        if (i < size - 1):
            G.add_edge(
                oddNumbers[i],
                oddNumbers[i + 1],
                color='b', 
                weight = 1
            )
            G.add_edge(
                evenNumbers[i],
                evenNumbers[i + 1], 
                color='g', 
                weight = 1
            )
        else:
            G.add_node(i)
            

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
                color='y',
                weight=1
            )

def fiveNodes(size):
    number = 5
    for i in range(size):
        if (i > 0):
            G.add_edge(
                number - 5,
                number,
                color='m',
                weight=1
            )
        number += 5


G = nx.MultiDiGraph()
size = 20

wholeNumbers(size) # Red
evenNumbers(size) # Green
oddNumbers(size) # Blue
primesNumbers(size) # Yellow
fiveNodes(size) #
# oddEvenNumbers(size) # Even = Green, Odd = BLue

colors = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()

pos = nx.kamada_kawai_layout(G)
# nx.draw_networkx_nodes(G, pos)
# nx.draw_networkx_labels(G,pos)
# nx.draw_networkx_edges(
#     G, pos,
#     connectionstyle="arc3,rad=0.1"  # <-- THIS IS IT
# )
nx.draw(
    G, 
    pos,
    edge_color=colors, 
    width=list(weights),
    with_labels=True,
    node_color='lightgreen'
)
plt.show()

# G.add_edge(0,1,color='r',weight=2)
# G.add_edge(1,2,color='g',weight=4)
# G.add_edge(2,3,color='b',weight=6)
# G.add_edge(3,4,color='y',weight=3)
# G.add_edge(4,0,color='m',weight=1)