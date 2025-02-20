import string

class Tree:
    def __init__(self, val):
        self.children = []
        self.val = val

    @classmethod
    def serialize(cls, root):
        if not root:
            return ""

        output = ""
        output += f"{root.val}"

        if not root.children:
            return output

        output += "("
        num_children = len(root.children)
        for (idx, child) in enumerate(root.children):
            output += Tree.serialize(child)
            if idx < num_children - 1:
                output += ","
        output += ")"

        return output

    @classmethod
    def deserialize(cls, data):
        if not data:
            return None

        stack = []
        current = Tree('')
        for c in data:
            s = list(map(lambda s: s.val, stack))
            if c in string.ascii_letters:
                current.val += c
            elif c =='(':
                stack.append(current)
                current = Tree('')
            elif c == ',':
                stack[-1].children.append(current)
                current = Tree('')
            elif c == ')':
                stack[-1].children.append(current)
                current = stack.pop()
            else:
                raise Exception("Malformed input")
        return current

def main():
    root = Tree('A')
    b = Tree('B')
    c = Tree('C')
    d = Tree('D')
    e = Tree('E')
    f = Tree('F')
    i = Tree('I')
    g = Tree('G')
    h = Tree('H')
    j = Tree('J')
    k = Tree('K')

    root.children = [b, c, d]
    b.children = [e, f]
    d.children = [i, g, h, j]
    f.children = [k]

    raw = Tree.serialize(root)
    tree = Tree.deserialize(raw)
    back_again = Tree.serialize(tree)
    print(raw)
    print(back_again)
    assert raw == back_again


if __name__ == '__main__':
    main()

