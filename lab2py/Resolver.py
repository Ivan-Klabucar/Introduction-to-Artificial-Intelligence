from HelperFunctions import *

class Resolver:
    def __init__(self, premises, goal): # premises are not const
        self.premises = premises
        self.sos = goal.negate()
        self.first_sos = list(self.sos)
        self.goal = goal
        self.solution = None
        
        simplify_clauses(self.premises)
        simplify_clauses(self.sos)
    
    def resolve_step(self, new_clauses, x, y):
        resolvents, is_there_nil = x.resolve(y)
        if is_there_nil:
            for x in resolvents:
                if x.nil: self.solution = x
            return True
        new_clauses.update(resolvents)
        return False

    def deduce(self):
        while True:
            new_clauses = set()
            for x in self.sos:
                for y in self.sos:
                    if self.resolve_step(new_clauses, x, y): return True
            
            for x in self.sos:
                for y in self.premises:
                    if self.resolve_step(new_clauses, x, y): return True
            if new_clauses.issubset(set.union(self.premises, self.sos)): return False
            self.sos.update(new_clauses)
                