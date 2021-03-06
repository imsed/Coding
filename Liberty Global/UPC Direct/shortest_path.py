__author__ = 'ismayl'
from lxml import etree
from    priodict        import  priorityDictionary
import pydot
import random
import datetime
import time
from multiprocessing import Pool
from itertools import product
def     dijkstra(G, start, end=None):
        """
        Find shortest paths from the  start vertex to all vertices nearer than or equal to the end.
        For any vertex v, G[v] is itself a dictionary, indexed by the neighbors of v.  For any edge v->w, G[v][w] is the length of the edge.
        The output is a pair (D,P) where D[v] is the distance from start to v and P[v] is the predecessor of v along the shortest path from s to v.
        """

        D               = {}                    # dictionary of final distances.
        P               = {}                    # dictionary of predecessors.
        Q               = priorityDictionary()  # estimated distances of non-final vertices.
        Q[start]        = 0

        for v in Q:
                D[v] = Q[v]
                if v == end: break
                for w in G[v]:
                        vwLength = D[v] + G[v][w][0]
                        if w in D:
                                if vwLength < D[w]:
                                        raise ValueError, "Dijkstra: found better path to already-final vertex"
                        elif w not in Q or vwLength < Q[w]:
                                Q[w] = vwLength
                                P[w] = (v,G[v][w][1])

        return  ( D, P )
def     shortest_path(G, source, destination):
        """
        Find a single shortest path from the given start vertex to the given end vertex.
        The output is a list of the vertices in order along the shortest path.
        """

        D,P = dijkstra(G,source,destination)
        Path = []
        end=(destination,"")
        while 1:
                Path.append(end)
                if end[0] == source: break
                end = P[end[0]]
        Path.reverse()

        return  Path
def     isis_database_dict(isis_db_xml_file):
        tree = etree.parse(isis_db_xml_file)
        database = {}
        for db_entry in tree.xpath("//isis-database-entry"):
            hostname = " ".join(db_entry.xpath("./lsp-id/text()")).strip("\n").split('.')[0].split('-re')[0]
            try:
                    database[hostname]
            except KeyError:
                    database[hostname] = {}
            for re_tlv in db_entry.xpath('./isis-tlv/reachability-tlv') :
                    neighbor_hostname = " ".join(re_tlv.xpath("./address-prefix/text()")).strip("\n").split('.')[0].split('-re')[0]
                    neighbor_metric = int(" ".join(re_tlv.xpath("./metric/text()")).strip("\n"))
                    neighbor_local_prefix = " ".join(re_tlv.xpath("./isis-reachability-subtlv/address/text()")).strip("\n")
                    try:
                            int(neighbor_hostname)
                            break
                    except ValueError:
                            if (neighbor_hostname not in database[hostname]) or (database[hostname][neighbor_hostname][0] > neighbor_metric):
                                database[hostname].update({neighbor_hostname: (neighbor_metric, neighbor_local_prefix)})
        return database
def     upc_direct_graph(file,direction):
        f = open(file)
        nodes = f.readlines()
        f.close()
        G = pydot.Dot(graph_type='digraph')
        database = isis_database_dict("show_isis_database_extensive.xml")
        hub = nodes[0].strip('\n')
        for h in nodes:
                spoke = h.strip('\n')
                if direction == "hub_to_spoke":
                        path = shortest_path(database, hub, spoke)
                elif direction == "spoke_to_hub":
                        path = shortest_path(database, spoke, hub)
                G.add_node(pydot.Node(spoke, fontsize="15.0", shape='none', image='/home/ismayl/python_scripts/Juniper/router-icon.jpg'))
                color = "#%03x" % random.randint(0, 0xFFFFFF)
                for i in range(len(path)-1):
                        G.add_node(pydot.Node(path[i][0], fontsize="15.0",  shape='none', image='/home/ismayl/python_scripts/Juniper/router-icon.jpg'))
                        G.add_edge(pydot.Edge(path[i][0], path[i+1][0], label=path[i][1], labelloc="t", labelfontcolor=color, fontsize="10.0", color=color))
        return G
def     draw_graph(args):
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')
        upc_direct_graph(args[0],args[1]).write_png(str(args[0]).split("hosts.txt")[0]+args[1]+"@"+st+".png")
        overlap=[]
def     graph_contain(n,G):
        if n.get_name() in [node.get_name() for node in G.get_node_list()]:
                overlap.append(n.get_name())


if __name__ == '__main__':
        po = Pool()
        hosts_file = ('upc_direct_secondary_hosts.txt','upc_direct_primary_hosts.txt')
        direction = ("hub_to_spoke","spoke_to_hub")
        po.map(draw_graph,((f,d) for f,d in product(hosts_file,direction)))
        G = []
        for f,d in product(hosts_file,direction):
                G.append(upc_direct_graph(f,d))
        print len(G)
        Pool().map(graph_contain,((n,g) for n,g in product(G[0].get_node_list(),G[2])))







#G = isis_database_dict("show_isis_database_extensive.xml")
#print G["nl-ams05a-rc1"]
#print  shortest_path(G, "nl-ams05a-rc1", "pl-waw04a-ra18")

