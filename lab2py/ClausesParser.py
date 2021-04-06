from Clause import *

class ClausesParser:
    def __init__(self, path_to_file):
        self.path = path_to_file
    
    def load_lines_and_remove_comments(self):
        lines = []
        with open(self.path, 'r') as clauses_file:
            for l in clauses_file.readlines():
                if l[0] != '#':
                    lines.append(l.strip().lower())
        return lines

    def parse(self):
        lines = self.load_lines_and_remove_comments()
        return set([Clause(l) for l in lines[:-1]]), Clause(lines[-1])

