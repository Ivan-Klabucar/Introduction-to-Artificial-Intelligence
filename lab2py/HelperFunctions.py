def delete_from_set_if(main_set, condition):
    for elem in list(main_set):
        if condition(elem):
            main_set.discard(elem)

def negate_atom(atom):
    if atom[0] == '~':
        return atom[1:]
    else:
        return '~' + atom

def simplify_clauses(clauses):
    delete_from_set_if(clauses, lambda x: x.is_tautology())
    for x in list(clauses):
        for y in list(clauses):
            if not x == y and x.is_subsumed_by(y):
                clauses.discard(x)
                break

class Counter:
    def __init__(self, value):
        self.value = value
    
    def post_inc(self):
        self.value += 1
        return self.value - 1

def print_knowledge_base(knowledge):
    print('Constructed with knowledge:')
    for k in knowledge:
        print(k)
    print()

def print_list_of_clauses(clauses_list):
    for x in clauses_list:
        finish = '\n'
        if x.parents: finish = ' (' + ', '.join([str(p.num) for p in x.parents]) + ')' + finish
        print(f'{x.num}. {x}', end=finish)

def print_deduction(resolver):    
    if not resolver.solution:
        print(f'[CONCLUSION]: {resolver.goal} is unknown')
        return
    
    cnt = Counter(1)
    starting_clauses = set(resolver.premises)
    starting_clauses_list = list(starting_clauses)
    starting_clauses.update(resolver.first_sos)
    starting_clauses_list.extend(resolver.first_sos)
    for x in starting_clauses_list: x.set_counter(cnt)
    print_list_of_clauses(starting_clauses_list)
    print('===============')
    deduction_clauses = list()
    queue = [resolver.solution]
    while queue:
        curr_clause = queue.pop(0)
        deduction_clauses.append(curr_clause)
        if curr_clause.parents: 
            for x in curr_clause.parents:
                if x not in starting_clauses: queue.append(x)
    deduction_clauses.reverse()
    for x in deduction_clauses: x.set_counter(cnt)
    print_list_of_clauses(deduction_clauses)
    print('===============')
    print(f'[CONCLUSION]: {resolver.goal} is true')

def print_deduction2(resolver):
    if not resolver.solution:
        print(f'[CONCLUSION]: {resolver.goal} is unknown')
        return

    starting_clauses = set(resolver.premises)
    starting_clauses.update(resolver.first_sos)
    starting_clauses_list = list(resolver.first_sos)

    deduction_clauses = list()
    queue = [resolver.solution]
    while queue:
        curr_clause = queue.pop(0)
        deduction_clauses.append(curr_clause)
        if curr_clause.parents: 
            for x in curr_clause.parents:
                if x not in starting_clauses: 
                    queue.append(x)
                elif x not in starting_clauses_list:
                    starting_clauses_list.append(x)
    deduction_clauses.reverse()
    starting_clauses_list.reverse()
    cnt = Counter(1)
    for x in starting_clauses_list: x.set_counter(cnt)
    for x in deduction_clauses: x.set_counter(cnt)
    print_list_of_clauses(starting_clauses_list)
    print('===============')
    print_list_of_clauses(deduction_clauses)
    print('===============')
    print(f'[CONCLUSION]: {resolver.goal} is true')


    
    



