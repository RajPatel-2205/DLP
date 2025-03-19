class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")  # Remove spaces
        self.index = 0

    def parse_S(self):
        if self.match('a'):
            return True
        elif self.match('('):
            if self.parse_L() and self.match(')'):
                return True
            return False
        return False

    def parse_L(self):
        if self.parse_S():
            return self.parse_L_prime()
        return False

    def parse_L_prime(self):
        if self.match(','):
            if self.parse_S():
                return self.parse_L_prime()
            return False
        return True  # ε (epsilon case)

    def match(self, char):
        if self.index < len(self.input) and self.input[self.index] == char:
            self.index += 1
            return True
        return False

    def is_valid(self):
        return self.parse_S() and self.index == len(self.input)


def validate_string(input_string):
    parser = RecursiveDescentParser(input_string)
    if parser.is_valid():
        print("Valid string")
    else:
        print("Invalid string")


# Test cases
inputs = ["a", "(a)", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)", "a)", "(a a)", "a a", "(a,a),a"]
for test in inputs:
    print(f"Input: {test}")
    validate_string(test)
