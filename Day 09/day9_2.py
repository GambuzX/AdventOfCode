import re

file = open("input.txt")
input_line = file.read()
file.close()

players_n = int(re.search("([0-9]*)(\splayers)", input_line).group(1))
last_marble = int(re.search("([0-9]*)(\spoints)", input_line).group(1)) * 100

class Node:
	def __init__(self, data):
		self.data = data
		self.last = None
		self.next = None

players = [0 for i in range(players_n)]
node0 = Node(0)
node1 = Node(1)
node0.next = node1
node0.last = node1
node1.next = node0
node1.last = node0
current_node = node1

for marble in range(2, last_marble):
	if marble % 23 == 0:
		for i in range(7):
			current_node = current_node.last
		players[marble % players_n] += marble + current_node.data
		current_node.last.next = current_node.next
		current_node.next.last = current_node.last
		current_node = current_node.next
	else:
		newNode = Node(marble)
		newNode.last = current_node.next
		newNode.next = current_node.next.next
		current_node.next.next.last = newNode
		current_node.next.next = newNode
		current_node = newNode

print(max(players))