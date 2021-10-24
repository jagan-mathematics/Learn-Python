N = 6
R = 11

str1 = ['L', 'R', 'LL', 'LR', 'RR']
val = [14, 28, 7, 8 , 14]


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.m = []

    def insert(self, data, s):
        if self.data:
            if s[0] == 'L':
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data, s[1:])
            elif s[0] == 'R':
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data, s[1:])
        else:
            self.data = data

    def len(self, root):
        count = 0
        if root.left:
            count += 1
        if root.right:
            count += 1
        return count


    def check_factor(self, root):
        if self.len(root) == 2:
            return (root.left.data % root.right.data == 0) or (root.right.data % root.left.data == 0)


    def find_magic_node(self):
        if self.check_factor(self):
            self.m.append(self.data)
        if self.left:
            self.m.extend(self.left.find_magic_node())
        if self.right:
            self.m.extend(self.right.find_magic_node())
        return self.m



root = Node(R)

for s, v in zip(str1, val):
    root.insert(v, s)



print(sum(root.find_magic_node()))



