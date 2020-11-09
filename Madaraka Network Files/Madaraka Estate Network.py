import networkx as nx
import matplotlib.pyplot as plt
from bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","STC","Phase2","J1","Mada","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SportsComplex","Siwaka",weight="UnkRoad450m")
G.add_edge("Siwaka","Ph.1A",weight="SangaleRd10m")
G.add_edge("Siwaka","Ph.1B",weight="SangaleLink230m")
G.add_edge("Ph.1A","Ph.1B",weight="ParkingWalkWay100m")
G.add_edge("Ph.1A","Mada",weight="SangaleRd850m")
G.add_edge("Ph.1B","Phase2",weight="KeriRd112m")
G.add_edge("Phase2","J1",weight="KeriRd600m")
G.add_edge("J1","Mada",weight="SangaleRd200m")
G.add_edge("Ph.1B","STC",weight="KeriRd50m")
G.add_edge("Phase2","STC",weight="STCwalkway50m")
G.add_edge("Phase2","Phase3",weight="KeriRd500m")
G.add_edge("Phase3","ParkingLot",weight="HimaGardensRd350m")
G.add_edge("Mada","ParkingLot",weight="langataRd700m")
G.add_edge("STC","ParkingLot",weight="LibraryWalkWay250m")

#position the nodes to resemble Nairobis map
G.nodes["SportsComplex"]['pos']=(-17,12)
G.nodes["Siwaka"]['pos']=(-2,12)
G.nodes["Ph.1A"]['pos']=(8,12)
G.nodes["Ph.1B"]['pos']=(8,-10)
G.nodes["Phase2"]['pos']=(17,-10)
G.nodes["J1"]['pos']=(25,-10)
G.nodes["Mada"]['pos']=(35,-10)
G.nodes["STC"]['pos']=(8,-25)
G.nodes["Phase3"]['pos']=(25,-25)
G.nodes["ParkingLot"]['pos']=(25,-40)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['peru' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['peru' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
