import random
from collections import defaultdict
import numpy as np
import pandas as pd

#Κλαση που αναπαριστα το αντικειμενο graph
class Graph:


    #συναρτηση ωστε να βρεθει ο κομβος με την μικροτερη αποσταση, απο τους κομβους που εξακολουθουν να υπαρχουν στην ουρα προτεραιοτητας
    def minDistance(self, dist, queue):
        # αρχικοποιει την min αξια se apeiro  kai ton min index se -1
        minimum = float("Inf")
        min_index = -1

        # Απο τον πινακα αποστασης διαλεξε ενα το οποιο εχει την μικροτερη αξια και ειναι ακομα στην ουρα προτεραιοτητας

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    #  Συναρτηση που εκτυπωνει τα συντομοτερα μονοπατια απο την πηγη J χρησιμοποιωντας πινακα γονεα

    def printPath(self, parent, j, l):
        #Επιστρεφει μια λιστα απο τον προορισμο στην πηγη η βασικη υποθεση ειναι j=source

        if parent[j] == -1:
            return l
        else:
            l.append(j)
            return self.printPath(parent, parent[j], l)

    #συναρτηση που εκτυπωνει τα ζητουμενα του αλγοριθμου
    #η εκτυπωση δειχνει τον αρχικο κομβο και την αποσταση απο ολους τους αλλους κομβους και απο ποιους κομβους
    #πηγε εκει. Δεν συμπεριλαμβανει τον αρχικο κομβο δηλαδη αν δειτε [2,14] ξεκινησε απο το 0 πηγε στο 2 και μετα στο 14
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\t\t\tDistance from Source\t\tPath")

        for i in range(1, len(dist)):
            st = f"from {src}  to {i}\t\t\t\t{dist[i]}\t\t\t\t\t{self.printPath(parent, i, [])[::-1]}"

            print(st)

    '''Συναρτηση που εφαρμοζει τον djikstra χρησιμοποιωντας ως εισοδο πινακα γειτνιασης '''

    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])

        #  dist[i] κρατα
        # την πιο κοντινη αποσταστη  απο την πηγη στον κομβο i
        # αρχικοποιει ολες τις αποστασεις ως απειρο
        dist = [float("Inf")] * row

        # πινακας γονεας που κρατα το δεντρο για την κοντινοτερη  αποσταση
        parent = [-1] * row

        # η αποσταση της πηγης απο τον εαυτο της ειναι παντα 0
        dist[src] = 0

        # προσθεσε ολους τους κομβους στην λιστα
        queue = []
        for i in range(row):
            queue.append(i)

        # βρισκει τις πιο συντομες διαδρομες για ολους τους κομβους οσο υπαρχουν στοιχεια στην λιστα

        while queue:

            # διαλεγει την κοντινοτερη αποσταση απο το σετ των κομβων που βρισκονται ακομα στην ουρα προτεραιοτητας

            u = self.minDistance(dist, queue)

            # αφαιρει το μικροτερο στοιχειο
            queue.remove(u)

            #ενημερωνει την αξια της αποστασης και τον δεικτη του γονεα των γειτονικων κομβων του επιλεγμενου κομβου
            #ελεγχει οσους κομβους ειναι ακομα στην ουρα


            for i in range(col):
                '''ενημερωνει την μεταβλητη dist[i] αν ειναι στην ουρα και υπαρχει ακμη απο τον κομβο u στον κομβο i 
                και το συνολικο βαρος απο την πηγη στο i μεσω του u  ειναι μικροτερη απο την τωρινη αξια της dist[i]
                '''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u




        #εκτυπωνει την λυση
        self.printSolution(dist, parent)


g = Graph() #δημιουργει το γραφημα ως αντικειμενο
graph10 = np.load("graph_weight_until_10.npy").tolist()  #φορτωνει τα διαγραμματα με τυχαια βαρη 10,25,50,100
                                               #τα μετατρεπει σε λιστα ως εισοδο για τον αλγοριθμο στην ουσια ειναι Nested list
graph25 = np.load("graph_weight_until_25.npy").tolist()
graph50 = np.load("graph_weight_until_50.npy").tolist()
graph100 = np.load("graph_weight_until_100.npy").tolist()




for xx in range(5):#εκτελει 5 φορες για το γραφο 1 και απο κατω συνεχιζω για τους υπολοιπους
    print(f"==================================================================\nExecution of graph with random weights up to 10: {xx+1}")
    g.dijkstra(graph10, 0)  #αναθετει το αντικειμενο graph με την σχεση g=Graph() στην συναρτηση του αλγοριθμου dijkstra.

for xx in range(5):
    print(f"==================================================================\nExecution of graph with random weights up to 25: {xx+1}")
    g.dijkstra(graph25, 0)

for xx in range(5):
    print(f"==================================================================\nExecution of graph with random weights up to 50: {xx+1}")
    g.dijkstra(graph50, 0)

for xx in range(5):
    print(f"==================================================================\nExecution of graph with random weights up to 100: {xx+1}")
    g.dijkstra(graph100, 0)

