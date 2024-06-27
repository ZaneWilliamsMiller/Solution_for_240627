def check_parentheses(strings):
    results = []

    for s in strings:
        stack = []
        markers = [" "] * len(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    markers[i] = "?"

        for index in stack:
            markers[index] = "x"

        results.append(s)
        results.append("".join(markers))

    return results


if __name__ == "__main__":
    strings = ["bge)))))))))", "((IIII))))))", "()()()()(uuu", "))))UUUU((()"]

    results = check_parentheses(strings)
    for s in results:
        print(s)
