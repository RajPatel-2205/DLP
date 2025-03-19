from collections import defaultdict

class CFG:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())
        self.first = defaultdict(set)
        self.follow = defaultdict(set)
        self.start_symbol = list(productions.keys())[0]
        self.epsilon = 'ε'

    def compute_first(self):
        changed = True
        while changed:
            changed = False
            for nt, rules in self.productions.items():
                for rule in rules:
                    i = 0
                    while i < len(rule):
                        symbol = rule[i]
                        if symbol not in self.non_terminals:  # Terminal
                            if symbol not in self.first[nt]:
                                self.first[nt].add(symbol)
                                changed = True
                            break
                        else:  # Non-terminal
                            before = len(self.first[nt])
                            self.first[nt] |= (self.first[symbol] - {self.epsilon})
                            if self.epsilon in self.first[symbol]:
                                i += 1
                            else:
                                break
                            if before != len(self.first[nt]):
                                changed = True
                    else:
                        if self.epsilon not in self.first[nt]:
                            self.first[nt].add(self.epsilon)
                            changed = True

    def compute_follow(self):
        self.follow[self.start_symbol].add('$')
        changed = True
        while changed:
            changed = False
            for nt, rules in self.productions.items():
                for rule in rules:
                    follow_temp = self.follow[nt].copy()
                    for symbol in reversed(rule):
                        if symbol in self.non_terminals:
                            before = len(self.follow[symbol])
                            self.follow[symbol] |= follow_temp
                            if self.epsilon in self.first[symbol]:
                                follow_temp |= (self.first[symbol] - {self.epsilon})
                            else:
                                follow_temp = self.first[symbol]
                            if before != len(self.follow[symbol]):
                                changed = True
                        else:
                            follow_temp = {symbol}

    def display_sets(self):
        print("First Sets:")
        for nt in self.non_terminals:
            print(f"First({nt}) = {sorted(self.first[nt])}")
        print("\nFollow Sets:")
        for nt in self.non_terminals:
            print(f"Follow({nt}) = {sorted(self.follow[nt])}")

productions = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

cfg = CFG(productions)
cfg.compute_first()
cfg.compute_follow()
cfg.display_sets()