from database.DAO import DAO, getAllEdges
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate ={}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)
        allEdges = getAllEdges()
        for edge in allEdges:
            u = self._idMapFermate[edge.id_stazP]
            v = self._idMapFermate[edge.id_stazA]



    @property
    def fermate(self):
        return self._fermate

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

