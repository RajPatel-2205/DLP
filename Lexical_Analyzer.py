import re

# Define token categories
KEYWORDS = {"int", "char", "return"}  # Extend this as needed
OPERATORS = {"=", "+", "-", "*", "/", "%"}
PUNCTUATION = {"(", ")", "{", "}", ",", ";"}

# Regular expressions for token matching
IDENTIFIER_REGEX = r"[a-zA-Z_][a-zA-Z_0-9]*"
CONSTANT_REGEX = r"\b\d+\b"
STRING_REGEX = r"'.'"
COMMENT_REGEX = r"//.*?$|/\*.*?\*/"

# Symbol table to store identifiers
symbol_table = set()

def tokenize(code):
    # Remove comments
    code = re.sub(COMMENT_REGEX, "", code, flags=re.DOTALL)
    
    tokens = []
    errors = []
    modified_code = ""
    words = re.split(r'(\s+|"|\'|[{}(),;+*/%-])', code)
    
    for word in words:
        if not word or word.isspace():
            continue
        elif word in KEYWORDS:
            tokens.append(("Keyword", word))
        elif word in OPERATORS:
            tokens.append(("Operator", word))
        elif word in PUNCTUATION:
            tokens.append(("Punctuation", word))
        elif re.fullmatch(CONSTANT_REGEX, word):
            tokens.append(("Constant", word))
        elif re.fullmatch(STRING_REGEX, word):
            tokens.append(("String", word))
        elif re.fullmatch(IDENTIFIER_REGEX, word):
            tokens.append(("Identifier", word))
            symbol_table.add(word)
        else:
            errors.append(f"Lexical Error: {word}")
            
        modified_code += word + " "
    
    return tokens, errors, modified_code.strip()

# Sample input code
code = """
int main() {
    int a = 5 , 7H;
    // assign value
    char b = 'x';
    /* return value */
    return a + b;
}
"""

tokens, errors, modified_code = tokenize(code)

print("TOKENS")
for token in tokens:
    print(f"{token[0]}: {token[1]}")

print("\nSymbol Table:", symbol_table)
print("\nErrors:", errors)
print("\nModified Code:")
print(modified_code)