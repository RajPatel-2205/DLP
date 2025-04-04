from collections import defaultdict

class LL1Parser:
    def __init__(self, productions, first, follow):
        self.productions = productions
        self.first = first
        self.follow = follow
        self.non_terminals = list(productions.keys())
        self.terminals = set()
        self.table = defaultdict(dict)
        self.epsilon = 'ε'
        self.build_parsing_table()

    def build_parsing_table(self):
        for nt in self.productions:
            for rule in self.productions[nt]:
                first_set = self.get_first_set(rule)
                for terminal in first_set:
                    if terminal != self.epsilon:
                        if terminal in self.table[nt]:
                            print("Grammar is not LL(1) due to conflict in", nt)
                            return
                        self.table[nt][terminal] = rule
                if self.epsilon in first_set:
                    for terminal in self.follow[nt]:
                        if terminal in self.table[nt]:
                            print("Grammar is not LL(1) due to conflict in", nt)
                            return
                        self.table[nt][terminal] = rule
        print("Grammar is LL(1)")
        self.display_parsing_table()

    def get_first_set(self, rule):
        first_set = set()
        for symbol in rule:
            if symbol in self.terminals or symbol == self.epsilon:
                first_set.add(symbol)
                break
            first_set |= (self.first[symbol] - {self.epsilon})
            if self.epsilon not in self.first[symbol]:
                break
        else:
            first_set.add(self.epsilon)
        return first_set

    def display_parsing_table(self):
        print("\nPredictive Parsing Table:")
        for nt, rules in self.table.items():
            for terminal, rule in rules.items():
                print(f"M[{nt}, {terminal}] = {rule}")

    def validate_string(self, input_string):
        input_string += '$'
        stack = ['$', self.non_terminals[0]]
        index = 0
        while stack:
            top = stack.pop()
            if top == input_string[index]:
                index += 1
            elif top in self.table and input_string[index] in self.table[top]:
                rule = self.table[top][input_string[index]]
                if rule != [self.epsilon]:
                    stack.extend(reversed(rule))
            else:
                print("Invalid string")
                return
        print("Valid string")

# Grammar definition
productions = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

first = {
    'S': {'a', 'b', '(', 'c'},
    'A': {'a', 'ε'},
    'B': {'b', 'ε'},
    'C': {'(', 'c'},
    'D': {'a', '('}
}

follow = {
    'S': {')', '$'},
    'A': {'b', '(', ')', '$'},
    'B': {'c', ')', '$'},
    'C': {')', '$'},
    'D': {')', '$'}
}

parser = LL1Parser(productions, first, follow)

# Test cases
inputs = ["abc", "ac", "(abc)", "c", "(ac)", "a", "( )", "(ab)", "abcabc", "b"]
for test in inputs:
    print(f"Input: {test}")
    parser.validate_string(test)