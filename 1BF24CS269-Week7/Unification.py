
# Week 7: First Order Logic - Unification

# Check whether a term is a variable
def is_variable(term):
    return term.startswith('?') or (
        term.isalpha() and term[0].islower()
    )

# Apply substitutions to a term
def substitute(term, subs):
    while term in subs:
        term = subs[term]
    return term

# Check occurs condition
def occurs(variable, term, subs):
    term = substitute(term, subs)

    if variable == term:
        return True

    if '(' in term:
        args = term[term.index('(') + 1:-1].split(',')
        return any(occurs(variable, arg.strip(), subs)
                   for arg in args)

    return False

# Unification algorithm
def unify(x, y, subs):

    x = substitute(x, subs)
    y = substitute(y, subs)

    if x == y:
        return subs

    if is_variable(x):
        if occurs(x, y, subs):
            return None
        subs[x] = y
        return subs

    if is_variable(y):
        if occurs(y, x, subs):
            return None
        subs[y] = x
        return subs

    # Check compound terms
    if '(' in x and '(' in y:
        name1 = x[:x.index('(')]
        name2 = y[:y.index('(')]

        if name1 != name2:
            return None

        args1 = x[x.index('(') + 1:-1].split(',')
        args2 = y[y.index('(') + 1:-1].split(',')

        if len(args1) != len(args2):
            return None

        for a, b in zip(args1, args2):
            subs = unify(a.strip(), b.strip(), subs)

            if subs is None:
                return None

        return subs

    return None


# Main program
print("First Order Logic - Unification")

expr1 = "Knows(x, John)"
expr2 = "Knows(Mary, y)"

print("Expression 1:", expr1)
print("Expression 2:", expr2)

# Extract predicate arguments
args1 = expr1[expr1.index('(') + 1:-1].split(',')
args2 = expr2[expr2.index('(') + 1:-1].split(',')

if expr1[:expr1.index('(')] != expr2[:expr2.index('(')]:
    print("Unification Failed: Predicates do not match.")

elif len(args1) != len(args2):
    print("Unification Failed: Different number of arguments.")

else:
    substitution = {}

    for a, b in zip(args1, args2):
        substitution = unify(a.strip(), b.strip(), substitution)

        if substitution is None:
            break

    if substitution is None:
        print("Unification Failed.")
    else:
        print("Unification Successful!")
        print("Most General Unifier (MGU):")

        for variable, value in substitution.items():
            print(variable, "=", substitute(value, substitution))
