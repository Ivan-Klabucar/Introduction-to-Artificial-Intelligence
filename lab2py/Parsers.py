from Clause import Clause
from Instruction import Instruction

class Parser:
    def __init__(self, path_to_file):
        self.path = path_to_file
    
    def load_lines_and_remove_comments(self):
        lines = []
        with open(self.path, 'r') as clauses_file:
            for l in clauses_file.readlines():
                if l[0] != '#':
                    lines.append(l.strip().lower())
        return lines

class ClausesParser(Parser):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)

    def parse(self):
        lines = self.load_lines_and_remove_comments()
        return set([Clause(l) for l in lines[:-1]]), Clause(lines[-1])

class CookingKnowledgeParser(Parser):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
    
    def parse_cooking_knowledge(self):
        lines = self.load_lines_and_remove_comments()
        return set([Clause(l) for l in lines])

class InstructionParser(Parser):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
    
    def parse_instructions(self):
        lines = self.load_lines_and_remove_comments()
        return [Instruction(l) for l in lines]

