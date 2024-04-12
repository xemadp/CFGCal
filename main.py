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
        simpleruleset = {}
        for line in ruleset:
            line = line.strip().split('->')
            var = line[0].strip()
            simpleruleset[var] = [t.strip() for t in line[1].split('|')]
    return simpleruleset


def flattenList(nestedList):
    flatList = []
    for sublist in nestedList:
        for item in sublist:
            flatList.append(item)
    return flatList

def evaluate(rules, var):
    srs = simplifyRuleset(rules)
    if var not in srs:  # If var is a terminal, return it
        return [var]
    result = []
    for v in srs[var]:  # For each production rule of the variable
        expanded_string = []
        for symbol in v.split():
            expanded_symbols = evaluate(rules, symbol)
            if len(expanded_symbols) == 1 and expanded_symbols[0] == symbol:
                expanded_string.append(symbol)  # Terminal symbol, add as is
            else:
                expanded_string.extend(expanded_symbols)
        result.append("".join(expanded_string))
    return result

# Evaluate a given variable num times if possible.
def evalNum(rules, val, num):
    rules = simplifyRuleset("rules.txt")
    result = [val]  # Start with the initial variable
    for _ in range(num):
        new_result = []
        for string in result:
            new_strings = []
            variables_evaluated = False
            for i, symbol in enumerate(string):
                if symbol in rules:
                    variables_evaluated = True
                    for rule in rules[symbol]:
                        new_string = string[:i] + rule + string[i+1:]
                        new_strings.append(new_string)
            if not variables_evaluated:  # No variable found, append original string
                new_strings.append(string)
            new_result.extend(new_strings)
        result = new_result
    return result
