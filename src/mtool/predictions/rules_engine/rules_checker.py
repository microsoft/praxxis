"""
Rules are defined as:

([filename match(es)],[output match(es)],[notebooks to suggest])

if either left-hand list is empty, this is interpreted as "all"
"""

def rules_check(rules, filename, output):
    for rule in rules:
        if filename in rules[0] & output in rules[1]:
            return rules[2]
    return -1