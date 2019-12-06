import re


class Node:
    def __init__(self, nodeID):
        self.id = nodeID
        self.children = []
        self.parent = None

    def child_count(self):
        if len(self.children) == 0:
            return 0

        curr_count = len(self.children)
        for child in self.children:
            curr_count += child.child_count()

        return curr_count

    def paths(self):
        if len(self.children) == 0:
            return 0

        curr_count = self.child_count()
        for child in self.children:
            curr_count += child.paths()

        return curr_count

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, target):
        if self.id == target:
            return True

        for child in self.children:
            if child.find_child(target):
                return True
        return False

    def distance_to(self, target):
        if self.id == target:
            return 0

        min_dist = 999999
        for child in self.children:
            dist = child.distance_to(target)
            min_dist = min(min_dist, dist+1)

        return min_dist


def common_ancestor(node):
    return node.find_child("YOU") and node.find_child("SAN")


with open("input.txt", 'r') as handle:
    lines = handle.read().split('\n')

nodes = {}
for line in lines:
    res = re.split(r'\)', line)
    parent = res[0]
    child = res[1]

    if parent not in nodes.keys():
        nodes[parent] = Node(parent)

    if child not in nodes.keys():
        nodes[child] = Node(child)

    nodes[parent].add_child(nodes[child])
    nodes[child].parent = nodes[parent]


start = nodes["YOU"].parent.id
end = nodes["SAN"].parent.id

ancestor = nodes[start]
while not common_ancestor(ancestor):
    ancestor = ancestor.parent

print(ancestor.distance_to(start) + ancestor.distance_to(end))
