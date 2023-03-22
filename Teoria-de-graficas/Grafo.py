import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

edges= [['V3','V2'],['V3','V1'],['V3','V4'],['V2','V1'],['V1','V4']]
G.add_edges_from(edges)

print("Vertices de la grafica. ")
print(G.nodes())
print("Aristas de la grafrica. ")
print(G.edges())

pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels={('V3','V2'):'e5',('V3','V1'):'e4',('V3','V4'):'e1',\
                                                ('V2','V1'):'e3',('V1','V4'):'e2'}, font_color='black')
plt.show()