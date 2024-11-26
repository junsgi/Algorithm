class Node:
    def __init__(self, n):
        self.n = n
        self.target = 0
        self.children = []
    def drop(self):
        if not self.children:
            self.target += 1
            return self.n
        idx = self.target % len(self.children)
        self.target += 1
        return self.children[idx].drop()
def solution(edges, target):
    N = 0
    for i in edges:
        N = max(N, max(i))
    Tree = [Node(i) for i in range(N + 1)]
    for a, b in edges:
        Tree[a].children.append(Tree[b])
    for i in range(1, N + 1):
        Tree[i].children.sort(key = lambda x : x.n)
    freq = [0] * len(target)
    root = Tree[1]
    indexes = []
    while 1:
        idx = root.drop() - 1
        indexes.append(idx)
        freq[idx] += 1
        for j in range(len(target)):
            if freq[j] * 3 < target[j]:
                break
        else:
            break
    for i in range(1, len(freq)):
        if not freq[i]: continue
        if not(freq[i] <= target[i] <= freq[i] * 3):
            return [-1]
    answer = []
    for i in indexes:
        freq[i] -= 1
        for j in range(1, 4):
            if freq[i] <= target[i] - j <= freq[i] * 3:
                answer.append(j)
                target[i] -= j
                break
    return answer
