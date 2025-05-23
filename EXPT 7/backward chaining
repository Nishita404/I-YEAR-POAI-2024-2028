
facts = {
    'a': True,
    'b': True,
    'c': False
}


rules = [
    ('d', ['a', 'b']),  
    ('e', ['b', 'c']),  
    ('f', ['d', 'e'])   
]


def backward_chaining(goal, facts, rules, inferred=None):
    if inferred is None:
        inferred = {}
    
    
    if goal in facts:
        return facts[goal]
    if goal in inferred:
        return inferred[goal]

    
    for head, body in rules:
        if head == goal:
            if all(backward_chaining(cond, facts, rules, inferred) for cond in body):
                inferred[goal] = True
                return True

    
    inferred[goal] = False
    return False


goal = 'f'
if backward_chaining(goal, facts, rules):
    print(f"The goal '{goal}' can be achieved.")
else:
    print(f"The goal '{goal}' cannot be achieved.")
