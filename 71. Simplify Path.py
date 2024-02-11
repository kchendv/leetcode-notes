class Solution:
    def simplifyPath(self, path: str) -> str:
        cur = ""
        stack = []
        slash_mode = True
        for c in path:
            if c == '/':
                if not slash_mode:
                    if cur == "..":
                        if stack:
                            stack.pop()
                    elif cur != ".":
                        stack.append(cur)
                    cur = ""
                slash_mode = True
            else:
                slash_mode = False
                cur += c
        if not slash_mode:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != ".":
                stack.append(cur)

        return '/' + '/'.join(stack)
        