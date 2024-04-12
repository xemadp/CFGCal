# A program that reads in an input file rules.txt along with a Given Variable and evaluates it.

rules = "rules.txt"


# Find Variables and Terminals.
def findVT(rules):
    with open(rules,'r') as ruleset:
        chars = []
        varset = []
        termset = []
        for line in ruleset:
            line = line.strip().split('->')
            for word in line:
                for char in word.split('|'):
                    chars.append(char)

        for var in chars:
            if var.isupper():
                varset.append(var.strip())
            else:
                termset.append(var.strip())

        varset = list(set(varset))
        termset = list(set(termset))

    return varset,termset

# Simplify Ruleset to only one RHS at a time.
def simplifyRuleset(rules):
    with open(rules,'r') as ruleset:
        chars = []
        simpleruleset = {}
        for line in ruleset:
            line = line.strip().split('->')
            var = line[0].strip()
            simpleruleset[var.strip()] = []
            for t in line[1].split('|'):
                simpleruleset[var.strip()].append(t.strip())

    return simpleruleset
