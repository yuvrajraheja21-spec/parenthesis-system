class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                return False

        return not stack


if __name__ == "__main__":

    example = input("Enter the string to validate: ")

    print(f"{Solution().isValid(example)}")
