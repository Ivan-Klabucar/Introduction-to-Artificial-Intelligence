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


