import sys
from ClausesParser import *
from Resolver import *

task = sys.argv[1]
path_to_clauses = sys.argv[2]
if task == 'resolution':
    premises, possible_conclusion = ClausesParser(path_to_clauses).parse()
    r = Resolver(premises, possible_conclusion)
    res = r.deduce()
    if res:
        print(f'goal: {r.goal.atoms} is true')
    else:
        print(f'goal: {r.goal.atoms} is unknown')
