import numpy as np
import pandas as pd
import openpyxl


graph_1 = np.random.randint(low=0, high=10, size=(50, 50))  ## dhmiourgei enan pinaka 50x50
graph_2 = np.random.randint(low=0, high=25, size=(50, 50))
graph_3 = np.random.randint(low=0, high=50, size=(50, 50))
graph_4 = np.random.randint(low=0, high=100, size=(50, 50))


graph1= np.triu(graph_1, 1)
graph1 = graph1 + graph1.T - np.diag(np.diag(graph1)) #allazei tis times sta kelia wste o pinakas na einai summetrikos
# dhladh to keli sto (1,2) na exei thn idia timh me to keli sto (2,1)
np.save("graph_weight_until_10", graph1) #apothikeuei ton pinaka pou theloume
df_graph1 = pd.DataFrame(graph1)#metatrepei to numpy array se dataframe
file_name = 'graph_weight_until_10.xlsx' #to onoma tou arxeiou excel pou tha apothikeutei o pinakas geitniashs
df_graph1.to_excel(file_name)


graph2= np.triu(graph_2, 1)
graph2 = graph2 + graph2.T - np.diag(np.diag(graph2)) #allazei tis times sta kelia wste  o pinakas na einai summetrikos
# dhladh to keli sto (1,2) na exei thn idia timh me to keli sto (2,1)
np.save("graph_weight_until_25", graph2)#apothikeuei ton pinaka pou theloume
df_graph2 = pd.DataFrame(graph2)#metatrepei to numpy array se dataframe
file_name = 'graph_weight_until_25.xlsx' #to onoma tou arxeiou excel pou tha apothikeutei o pinakas geitniashs
df_graph2.to_excel(file_name)

graph3 = np.triu(graph_3, 1)
graph3 = graph3 + graph3.T - np.diag(np.diag(graph3)) #allazei tis times sta kelia wste  o pinakas na einai summetrikos
# dhladh to keli sto (1,2) na exei thn idia timh me to keli sto (2,1)
np.save("graph_weight_until_50", graph3)#apothikeuei ton pinaka pou theloume
df_graph3 = pd.DataFrame(graph3)#metatrepei to numpy array se dataframe
file_name = 'graph_weight_until_50.xlsx' #to onoma tou arxeiou excel pou tha apothikeutei o pinakas geitniashs
df_graph3.to_excel(file_name)#metatrepei kai apothikeuei ton pinaka geitniashs se excel

graph4 = np.triu(graph_4, 1)
graph4 = graph4 + graph4.T - np.diag(np.diag(graph4)) #allazei tis times sta kelia wste  o pinakas na einai summetrikos
# dhladh to keli sto (1,2) na exei thn idia timh me to keli sto (2,1)
np.save("graph_weight_until_100", graph4)
df_graph4 = pd.DataFrame(graph4)#metatrepei to numpy array se dataframe
file_name = 'graph_weight_until_100.xlsx' #to onoma tou arxeiou excel pou tha apothikeutei o pinakas geitniashs
df_graph4.to_excel(file_name)












