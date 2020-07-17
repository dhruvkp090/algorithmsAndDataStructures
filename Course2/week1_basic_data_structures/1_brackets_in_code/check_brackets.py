# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    top = -1
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(char = next, position = i))
            top += 1
        if next in ")]}":
            if top == -1:
                return i + 1
            else:
                if are_matching(opening_brackets_stack[top].char, next):
                    opening_brackets_stack.pop(top)
                    top -= 1
                else:
                    return i + 1
    if top == -1:
        return 'Success'
    else:
        return opening_brackets_stack[top].position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
