import heap_id
import nhpn
from queue import PriorityQueue
def node_by_name(nodes, city, state):
        for node in nodes:
            if node.state == state:#Checks if value if state matches before checking cities as there can be multiple citieswith same name
                if city in node.description:#checks if city in present in Nodes
                    return node #The node if it exists, or None otherwise.
        return None

def distance(node1, node2):
    latitude_diff = node1.latitude - node2.latitude #for distance calculation of latitude
    longitude_diff = node1.longitude - node2.longitude#for distance calculation of longitude
    return (latitude_diff**2 + longitude_diff**2)**.5# final distance calculation
"""
Algo For Shortest Path
Dijkstra(G,w,s) Users priority queue Q
Initialize(G,s)
S<-Nil
Q<-V[G]
while Q=Nil:
    do u<- extract_min(Q)
    s=s U (u)
    for each vertex v Adj[u]
        do Relax
Initialize
for v E V:
    d[v]<- inf
d[s]<-0
Relax(u,v,w)
if d[v]>d[u]+w(u,v)
    then d[v]<-d[u]+w(u,v)
    TT[v]<-u
"""



def shortest_path(nodes, edges, weight, s,t ):
    print(edges)
