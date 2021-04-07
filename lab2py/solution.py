import sys
from Parsers import ClausesParser, CookingKnowledgeParser, InstructionParser
from Resolver import *
from HelperFunctions import print_deduction, print_knowledge_base

task = sys.argv[1]
path_to_clauses = sys.argv[2]
if task == 'resolution':
    premises, possible_conclusion = ClausesParser(path_to_clauses).parse()
    resolver = Resolver(premises, possible_conclusion)
    resolver.deduce()
    print_deduction(resolver)
elif task == 'cooking':
    path_to_instructions = sys.argv[3]
    knowledge_base = CookingKnowledgeParser(path_to_clauses).parse_cooking_knowledge()
    instructions = InstructionParser(path_to_instructions).parse_instructions()
    print_knowledge_base(knowledge_base)
    for i in instructions:
        i.execute(knowledge_base)
