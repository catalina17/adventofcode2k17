import numpy as np
import re


# Node -> weight
nodes = {}
# Node -> is child
children = {}
# Node -> list of children
tree = {}


def DFS(node):
    sum_ws = nodes[node]
    child_ws = []

    for i in range(0, len(tree[node])):
        child_w = DFS(tree[node][i])
        sum_ws += child_w
        child_ws.append(child_w)

    (ws, counts) = np.unique(child_ws, return_counts=True)
    if len(counts) > 1:
        # We've found a subtree of a different sum
        other_w = None
        w = None

        if counts[0] == 1:
            idx1 = 0
            idx2 = 1
        else:
            idx1 = 1
            idx2 = 0

        child_idx = child_ws.index(ws[idx1])
        w = ws[idx1]
        other_w = ws[idx2]

        # Unbalanced node
        print(tree[node][child_idx],
              nodes[tree[node][child_idx]] + other_w - w)

    # All good so far, return sum of subtree
    return sum_ws


if __name__ == '__main__':
    f = open("day7.txt", "r")
    for line in f.readlines():
        print(line)
        words = re.findall(r"[\w]+", line)
        nodes[words[0]] = int(words[1])
        tree[words[0]] = []

        # See if current node has children
        if len(words) > 2:
            for i in range(2, len(words)):
                children[words[i]] = True
                tree[words[0]].append(words[i])

    for node in nodes:
        if not node in children:
            DFS(node)
            break
