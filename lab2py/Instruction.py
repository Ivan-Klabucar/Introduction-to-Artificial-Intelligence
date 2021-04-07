from Clause import Clause
from Resolver import Resolver
from HelperFunctions import print_cooking_deduction

class Instruction:
    def __init__(self, line):
        self.type = line[-1]
        self.clause = Clause(line[:-2])
    
    def addition(self, knowledge):
        knowledge.add(self.clause)
    
    def removal(self, knowledge):
        knowledge.discard(self.clause)
    
    def deduction(self, knowledge):
        resolver = Resolver(knowledge, self.clause)
        resolver.deduce()
        print_cooking_deduction(resolver)

    def execute(self, knowledge):
        print(f'User’s command: {self.clause} {self.type}')
        if self.type == '+':
            self.addition(knowledge)
        elif self.type == '-':
            self.removal(knowledge)
        elif self.type == '?':
            self.deduction(knowledge)
        else:
            raise Exception('Instruction type unknown.')
        print()