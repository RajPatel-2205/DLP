class DFA:
    def __init__(self, states, input_symbols, transitions, initial_state, accepting_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def accepts(self, string):
        current_state = self.initial_state

        for symbol in string:
            if symbol not in self.input_symbols:
                return False  
            current_state = self.transitions[current_state][symbol]

        return current_state in self.accepting_states

# DFA definition based on given problem
def dfa1():
    states = {1, 2, 3, 4}
    input_symbols = {'a', 'b'}
    transitions = {
        1: {'a': 2, 'b': 3},
        2: {'a': 1, 'b': 4},
        3: {'a': 4, 'b': 1},
        4: {'a': 3, 'b': 2},
    }
    initial_state = 1
    accepting_states = {2}

    return DFA(states, input_symbols, transitions, initial_state, accepting_states)

# Testcases implementation
def testcase_1(string):
    # String over 0 and 1 where every 0 is immediately followed by 11
    import re
    pattern = r'^(1|011)*$'
    return bool(re.fullmatch(pattern, string))

def testcase_2(string):
    # String over a, b, c and ends with same letters
    if len(string) < 2 or not all(c in 'abc' for c in string):
        return False
    return string[0] == string[-1]

def testcase_3(string):
    # String over lowercase alphabets and digits, starts with alphabets only
    if not string:
        return False
    if not string[0].isalpha():
        return False
    return all(c.isalnum() for c in string)

# Main execution
if __name__ == "__main__":
    # DFA Testing
    dfa = dfa1()
    test_strings_dfa = ["aab", "abba", "bbaa", "aa"]
    print("DFA Testing Results:")
    for s in test_strings_dfa:
        print(f"String '{s}' accepted by DFA? {dfa.accepts(s)}")

    # Testcases Testing
    print("\nTestcase 1 Results:")
    test_strings_tc1 = ["011", "1011", "111", "011011"]
    for s in test_strings_tc1:
        print(f"String '{s}' valid? {testcase_1(s)}")

    print("\nTestcase 2 Results:")
    test_strings_tc2 = ["ab", "aa", "bccb", "abcba"]
    for s in test_strings_tc2:
        print(f"String '{s}' valid? {testcase_2(s)}")

    print("\nTestcase 3 Results:")
    test_strings_tc3 = ["abc123", "123abc", "a1b2c3", "abc"]
    for s in test_strings_tc3:
        print(f"String '{s}' valid? {testcase_3(s)}")
