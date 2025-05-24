# Facts: The knowledge base containing information about facts
facts = {
    'a': True,
    'b': True,
    'c': False
}

# Rules: Each rule is a tuple (conclusion, conditions)
rules = [
    ('d', ['a', 'b']),  # d can be concluded if a and b are true
    ('e', ['b', 'c']),  # e can be concluded if b and c are true
    ('f', ['d', 'e'])   # f can be concluded if d and e are true
]

# Forward Chaining Function
def forward_chaining(facts, rules, goal):
    inferred = {k for k, v in facts.items() if v}  # Start with true facts
    new_inferred = set(inferred)  # Track newly inferred facts

    while new_inferred:
        current_inferred = set()
        for head, body in rules:
            if head not in inferred and all(fact in inferred for fact in body):
                current_inferred.add(head)
        if current_inferred:
            inferred.update(current_inferred)
            new_inferred = current_inferred
        else:
            new_inferred = set()  # No new facts can be inferred

    return goal in inferred

# Example Usage
goal = 'f'
if forward_chaining(facts, rules, goal):
    print(f"The goal '{goal}' can be achieved.")
else:
    print(f"The goal '{goal}' cannot be achieved.")
