from StateSpace import *
from Algorithms import *
from HeuristicChecker import *

#state_path = input("input path to state space: ")
#h_path = input("input path to heuristic: ")
state_path = "istra.txt"
h_path = "istra_heuristic.txt"
s = StateSpace(state_path, h_path)
print()

print('BFS:')
bfs_al = BFS(s)
bfs_al.solve()
print()

print('Uniform Cost Search:')
ucs_al = UniformCostSearch(s)
ucs_al.solve()
print()

print('A* Search:')
a_star_al = AStarSearch(s)
a_star_al.solve()
print()

print("Checking bad istra heuristic:")
s2 = StateSpace(state_path, "istra_pessimistic_heuristic.txt")
checker = HeuristicChecker()
checker.check_if_optimistic(s2)
print()
checker.check_if_consistent(s2)
print()