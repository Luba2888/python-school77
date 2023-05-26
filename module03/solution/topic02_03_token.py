def tokenize_expression(expression):
    operators = ['+', '-', '*', '/', '^', '(', ')', '=', '<', '>']
    tokens = []
    current_token = ""

    for char in expression:
        if char.isdigit() or char in operators:
            if current_token and not current_token.isdigit():
                tokens.append(current_token)
                current_token = ""
            current_token += char
        elif char != " ":
            current_token += char
        elif current_token:
            tokens.append(current_token)
            current_token = ""

    if current_token:
        tokens.append(current_token)

    return tokens
