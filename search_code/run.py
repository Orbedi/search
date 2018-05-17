# Search methods

import search

#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
ab = search.GPSProblem('B', 'A', search.romania)
print "Heuristica: ", search.estimacion_heuristica(ab).path()
print "Coste acumulado: ", search.coste_acumulado(ab).path()

ab = search.GPSProblem('C', 'F', search.romania)
print "Heuristica: ", search.estimacion_heuristica(ab).path()
print "Coste acumulado: ", search.coste_acumulado(ab).path()

ab = search.GPSProblem('Z', 'A', search.romania)
print "Heuristica: ", search.estimacion_heuristica(ab).path()
print "Coste acumulado: ", search.coste_acumulado(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450