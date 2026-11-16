
# Week 6: Propositional Logic - Truth Table Enumeration

from itertools import product

# Evaluate the Knowledge Base
def KB(P, Q):
    # KB: P AND (P implies Q)
    return P and ((not P) or Q)

# Evaluate the Query
def query(P, Q):
    # Query: Q
    return Q

# Truth Table Enumeration
def truth_table_entails():
    symbols = ['P', 'Q']
    entails = True

    print("P\tQ\tKB\tQuery")

    for values in product([True, False], repeat=2):
        P, Q = values

        kb_value = KB(P, Q)
        query_value = query(P, Q)

        print(f"{P}\t{Q}\t{kb_value}\t{query_value}")

        # Check whether KB is true and Query is false
        if kb_value and not query_value:
            entails = False

    if entails:
        print("\nKB entails the Query.")
    else:
        print("\nKB does not entail the Query.")

# Main program
truth_table_entails()
