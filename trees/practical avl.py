# Assignment 2-Part 3
# Implemetation

from collections import deque
import math

class Node:
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None
# Helper Function
# This function is O(n)
def reversechildren(node1,node2,level):
	if node1 is None and node2 is None:
		return
	if level % 2 == 0:
		temp = node1.value
		node1.value = node2.value
		node2.value = temp

	reversechildren(node1.l,node2.r,level+1)
	reversechildren(node1.r,node2.l,level+1)

# Part 3 starts here
# This function is O(n)
def visiting_floors(root):
	if root is None:
		return
	result = []
	q = []
	q.append(root)
	while(len(q)>0):
		# had to pass the intger as a string due since that's the datatype the test cases are using
		result.append(str(q[0].value))
		node = q.pop(0)
		if node.l != None:
			q.append(node.l)
		if node.r != None:
			q.append(node.r)
	return result

# This function is O(n)
def changing_room_numbers(root):
	#Step one -> Think of a way to know that you are on the odd level
	# if root.value == 1:
	# 	level = 0
	# else:
	# 	level = math.log(2,root.value)
	# 	level = math.floor(level)
	#Step two -> Think what you have to store inorder to make the mirror image of odd levels of the tree
	#Hint For Step two -> Odd level Nodes are the Children of the Even level nodes
	if root is None:
		return None
	reversechildren(root.l,root.r,0)
	return 


if __name__ == '__main__':

	''' Construct the following tree
				  1
			   /     \
			 /         \
		   2             3
		 /   \         /   \
		4     5       6     7
	  /  \    / \    / \    / \
	 8    9  10 11 12  13  14 15
	'''

	root = Node(1)
	root.l = Node(2)
	root.r = Node(3)
	root.l.l = Node(4)
	root.l.r = Node(5)
	root.r.l = Node(6)
	root.r.r = Node(7)
	root.l.l.l = Node(8)
	root.l.l.r = Node(9)
	root.l.r.l = Node(10)
	root.l.r.r = Node(11)
	root.r.l.l = Node(12)
	root.r.l.r = Node(13)
	root.r.r.l = Node(14)
	root.r.r.r = Node(15)

	# visiting_floors(root)
# Call your functions below this line of code
