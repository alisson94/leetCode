

def paren(list):

    stack = []

    for bracket in list:

        if bracket in ["(", "[", "{"]:
            stack.append(bracket)
            continue

        if bracket == ")":
            if stack[-1] == "(":
                stack.pop()
                continue

            return False

        if bracket == "]":
            if stack[-1] == "[":
                stack.pop()
                continue

            return False

        if bracket == "}":
            if stack[-1] == "{":
                stack.pop()
                continue

            return False

    if len(stack) == 0:
        return True

    return False


print(paren("([)]"))