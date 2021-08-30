def valid_parentheses(parens):
    p = []
    balanced = True
    index = 0
    while index < len(parens) and balanced:
        token = parens[index]
        if token == "(":
            p.append(token)
        elif token == ")":
            if len(p) ==0:
                balanced = False
            else:
                p.pop()

        index += 1

    return balanced and len(p) ==0

    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """