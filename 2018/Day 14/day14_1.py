n_recipes = 607331
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

for i in range(n_recipes):
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
    else:
        new_node = Node(int(total))
        nodes[-1].next = new_node
        new_node.prev = nodes[-1]
        new_node.next = nodes[0]
        nodes[0].prev = new_node
        nodes.append(new_node)

    for j in range(elf1.value + 1):
        elf1 = elf1.next
    for j in range(elf2.value + 1):
        elf2 = elf2.next

curr_node = nodes[0]
ret_string = ""
for i in range(n_recipes):
    curr_node = curr_node.next

for i in range(10):
    ret_string += str(curr_node.value)
    curr_node = curr_node.next

print(ret_string)

