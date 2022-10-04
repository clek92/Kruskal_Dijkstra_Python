#KRUSKAL MST
import numpy as np
import random
# θετει τους κομβους ως "δεντρα"-"γονεις" μεταφορικα κανει τον καθε κομβο ενα δεντρο
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


# δημιουργει την ενωση i kai j.Δηλαδη δημιουργει το συνολο ολων των ακμων του γραφηματος
# Δινει false αν i kai j Ειναι στο ιδιο set
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b



# Βρισκει  to kruskal-mst
def kruskalMST(cost):
    mincost = 0  # κοστος min MST

    # Αρχιζει η δημιουργια των ασυνδετων κομβων
    for i in range(V):
        parent[i] = i



    # Συμπεριλαμβανει τις ακμες με το βαρος μία-μία
    edge_count = 0
    while edge_count < V - 1:
        min = INF #το inf σημαινει απειρο
        a = -1
        b = -1

        for i in range(V):
            for j in range(V):
                if find(i) != find(j) and cost[i][j] < min:

                        min = cost[i][j]
                        a = i
                        b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min

    print("Minimum cost= {}".format(mincost))


graph10 = np.load("graph_weight_until_10.npy").tolist()
graph25 = np.load("graph_weight_until_25.npy").tolist()
graph50 = np.load("graph_weight_until_50.npy").tolist()
graph100 = np.load("graph_weight_until_100.npy").tolist()

V = 50
parent = [i for i in range(V)]
INF = float('inf')
graph_10 = []
graph_25 = []
graph_50 = []
graph_100 = []
for item in graph10:
    temp = []
    for i in item:
        if i == 0:
            temp.append(INF)
        else:
            temp.append(i)
    graph_10.append(temp)


for item in graph25:
    temp = []
    for i in item:
        if i == 0:
            temp.append(INF)
        else:
            temp.append(i)
    graph_25.append(temp)

for item in graph50:
    temp = []
    for i in item:
        if i == 0:
            temp.append(INF)
        else:
            temp.append(i)
    graph_50.append(temp)

for item in graph100:
    temp = []
    for i in item:
        if i == 0:
            temp.append(INF)
        else:
            temp.append(i)
    graph_100.append(temp)


cost1 = graph_10
cost2 = graph_25
cost3 = graph_50
cost4 = graph_100

#καλει την συναρτηση που υπολογιζει το Mst του Kruskal οσες φορες ζητησατε και εκτυπωνει τα αποτελεσματα
for xx in range(5):
    print(f"=================================\nExecution of graph with random weights up to 10: {xx+1}")
    kruskalMST(cost1)

for xx in range(5):
    print(f"=================================\nExecution of graph with random weight up to 25: {xx+1}")
    kruskalMST(cost2)

for xx in range(5):
    print(f"=================================\nExecution of graph with random weight up to 50: {xx+1}")
    kruskalMST(cost3)


for xx in range(5):
    print(f"=================================\nExecution of graph with random weight up to 100: {xx+1}")
    kruskalMST(cost4)



