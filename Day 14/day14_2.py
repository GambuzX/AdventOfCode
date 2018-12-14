class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


first = Node(3)
second = Node(7)
first.next = second
first.prev = second
second.next = first
second.prev = first

nodes = [first, second]
elf1 = first
elf2 = second

node_string = str(first.value) + str(second.value)
str_to_match = "607331"

for i in range(100000000):
    total = str(elf1.value + elf2.value)
    if len(total) > 1:
        node1 = Node(int(total[0]))
        node2 = Node(int(total[1]))
        nodes[-1].next = node1
        node1.prev = nodes[-1]
        node1.next = node2
        node2.prev = node1
        node2.next = nodes[0]
        nodes[0].prev = node2
        nodes.append(node1)
        nodes.append(node2)

        node_string += str(node1.value) + str(node2.value)

    else:
        new_node = Node(int(total))
        nodes[-1].next = new_node
        new_node.prev = nodes[-1]
        new_node.next = nodes[0]
        nodes[0].prev = new_node
        nodes.append(new_node)

        node_string += str(new_node.value)

    for j in range(elf1.value + 1):
        elf1 = elf1.next
    for j in range(elf2.value + 1):
        elf2 = elf2.next

    if node_string.find(str_to_match, len(node_string)-10) != -1:
        print(node_string.find(str_to_match, len(node_string)-10))
        break
