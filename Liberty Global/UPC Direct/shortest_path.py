__author__ = 'ismayl'

from lxml import etree
def     dijkstra( G, start, end=None):
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
                        vwLength = D[v] + G[v][w]
                        if w in D:
                                if vwLength < D[w]:
                                        raise ValueError, "Dijkstra: found better path to already-final vertex"
                        elif w not in Q or vwLength < Q[w]:
                                Q[w] = vwLength
                                P[w] = v

        return  ( D, P )
def     shortest_path(G, start, end):
        """
        Find a single shortest path from the given start vertex to the given end vertex.
        The output is a list of the vertices in order along the shortest path.
        """

        D,P = dijkstra(G,start,end)
        Path = []
        while 1:
                Path.append(end)
                if end == start: break
                end = P[end]
        Path.reverse()

        return  Path
def     isis_database_dict(isis_db_xml_file):
        tree = etree.parse(isis_db_xml_file)
        for neighbor in tree.xpath("//isis-database-entry"):
            hostname = " ".join(neighbor.xpath("./lsp-id/text()")).strip("\n").split('.')[0]
            print hostname







isis_database_dict("/home/ismayl/show_isis_database_extensive.xml")
