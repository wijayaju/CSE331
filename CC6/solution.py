def balanced_brackets(string: str) -> bool:
    """
    Determines whether a given string contains balanced brackets.

    A string is considered balanced if:
    - Each opening bracket ('(', '[', '{') has a corresponding closing bracket (')', ']', '}').
    - The brackets are correctly nested and ordered.
    - There are no unmatched brackets.

    Args:
        string (str): The input string containing brackets and other characters.

    Returns:
        bool: True if the brackets in the string are balanced, False otherwise.

    Time Complexity:
        O(n) - The function iterates through the string once.

    Space Complexity:
        O(n) - In the worst case, all opening brackets are stored in the stack.

    Example:
        // >>> balanced_brackets("([])(){}(())()()")
        True
        // >>> balanced_brackets("([)]")
        False
    """
    # TODO: Implement this function
    if string[0] in ")]}":
        return False
    opens = []
    for ch in string:
        if ch == ')':
            if opens[-1] == '(':
                opens.pop()
            else:
                return False
        elif ch == ']':
            if opens[-1] == '[':
                opens.pop()
            else:
                return False
        elif ch == '}':
            if opens[-1] == '{':
                opens.pop()
            else:
                return False
        else:
            opens.append(ch)
    if len(opens) > 0:
        return False
    return True
