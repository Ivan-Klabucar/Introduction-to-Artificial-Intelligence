from HelperFunctions import negate_atom, simplify_clauses

class Clause:
    def __init__(self, line='', nil=False):
        self.atoms = set(line.lower().split(' v '))
        self.atoms.discard('')
        self.nil = nil

    def negate(self):
        return set([Clause(negate_atom(a)) for a in self.atoms])
    
    def is_tautology(self):
        if self.nil: return False
        checked = set()
        for a in self.atoms:
            if negate_atom(a) in checked:
                return True
            checked.add(a)
        return False
    
    def is_subsumed_by(self, clause):
        if clause.atoms.issubset(self.atoms): return True
        return False
    
    def resolve(self, other):
        result_resolvents = set()
        is_there_nil = False
        for x in self.atoms:
            if negate_atom(x) in other.atoms:
                new_resolvent = Clause(nil=True)
                new_resolvent.atoms.update(self.atoms)
                new_resolvent.atoms.update(other.atoms)
                new_resolvent.atoms.difference_update([x, negate_atom(x)])
                if new_resolvent.atoms: new_resolvent.nil = False 
                else: is_there_nil = True
                result_resolvents.add(new_resolvent)
        simplify_clauses(result_resolvents)
        return result_resolvents, is_there_nil
    
    def __eq__(self, other):
        if self.atoms.issubset(other.atoms) and other.atoms.issubset(self.atoms): return True
        return False
    
    def __hash__(self):
        l = list(self.atoms)
        l.sort()
        return hash(' v '.join(l))


    
