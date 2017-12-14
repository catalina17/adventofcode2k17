import numpy as np
import re


nodes = {}
children = {}
tree = {}
node = None


def DFS(node: str):
    # Reached a leaf, return its weight
    if len(tree[node]) == 0:
        return nodes[node]

    path_weights = []
    for i in range(0, tree[node]):
        path_weights.append(DFS(tree[node][i]))
        if node:
            return

    (vals, counts) = np.unique(path_weights, return_counts=True)
    idx = -1
    if len(vals) > 1:
        if counts[0] == 1:
            idx = list(vals).index()
        node =


if __name__ == '__main__':
    f = open("day7small.txt", "r")
    for line in f.readlines():
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
            print node
            break

    for key in tree:
        print(key, tree[key])
