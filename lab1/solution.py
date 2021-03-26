from StateSpace import *
from Algorithms import *
from HeuristicChecker import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--alg", help="bfs, ucs, ili astar")
parser.add_argument("--ss", help="putanja do opisnika prostora stanja")
parser.add_argument("--h", help="putanja do opisnika heuristike")
parser.add_argument("--check-optimistic", action="store_true", help="zastavica koja signalizira da se za danu heuristiku zeli provjeriti optimisticnost")
parser.add_argument("--check-consistent", action="store_true", help="zastavica koja signalizira da se za danu heuristiku zeli provjeriti konsistentnost")
args = parser.parse_args()

heuristic_path = None
if args.h:
    heuristic_path = args.h

state_space = StateSpace(args.ss, heuristic_path)
if args.alg:
    if args.alg == "bfs":
        bfs_al = BFS(state_space)
        bfs_al.solve()
    elif args.alg == "ucs":
        ucs_al = UniformCostSearch(state_space)
        ucs_al.solve()
    elif args.alg == "astar":
        a_star_al = AStarSearch(state_space)
        a_star_al.solve()
    else:
        raise Exception("Wrong value for argument --alg")


checker = HeuristicChecker()
if args.check_optimistic:
    checker.check_if_optimistic(state_space)
if args.check_consistent:
    checker.check_if_consistent(state_space)
