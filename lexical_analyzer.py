import re

# Token patterns
TOKEN_PATTERNS = [
    ("COMMENT", r"//.*|/\*[\s\S]*?\*/"),
    ("KEYWORD", r"\b(?:int|float|char|double|if|else|for|while|do|return|void|break|continue|switch|case|default)\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("CONSTANT", r"\b\d+(?:\.\d+)?\b"),
    ("STRING_LITERAL", r'"(?:\\.|[^"\\])*"'),
    ("CHAR_LITERAL", r"'(?:\\.|[^'\\])'"),
    ("OPERATOR", r"==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|&&|\|\||[+\-*/%=<>!&|]"),
    ("SEPARATOR", r"[(),;{}\[\]]"),
    ("SPECIAL_SYMBOL", r"[.:?]"),
    ("WHITESPACE", r"\s+"),
]


def lexical_analyzer(source_code):
    tokens = []
    position = 0

    combined_pattern = "|".join(
        f"(?P<{name}>{pattern})"
        for name, pattern in TOKEN_PATTERNS
    )

    pattern = re.compile(combined_pattern)

    while position < len(source_code):
        match = pattern.match(source_code, position)

        if not match:
            tokens.append(("UNKNOWN", source_code[position]))
            position += 1
            continue

        token_type = match.lastgroup
        token_value = match.group()

        if token_type != "WHITESPACE":
            tokens.append((token_type, token_value))

        position = match.end()

    return tokens


def display_tokens(tokens):
    print("\nLexical Analysis Result")
    print("-" * 50)
    print(f"{'Token Type':<20} Token")
    print("-" * 50)

    for token_type, token_value in tokens:
        print(f"{token_type:<20} {token_value}")


def count_tokens(tokens):
    counts = {}

    for token_type, _ in tokens:
        counts[token_type] = counts.get(token_type, 0) + 1

    return counts


def main():
    filename = "input.c"

    try:
        with open(filename, "r") as file:
            source_code = file.read()

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    tokens = lexical_analyzer(source_code)

    display_tokens(tokens)

    counts = count_tokens(tokens)

    print("\nToken Count")
    print("-" * 30)

    for token_type, count in counts.items():
        print(f"{token_type:<20} {count}")


if __name__ == "__main__":
    main()