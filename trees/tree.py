# Assignment 2-Part 1
# BST

from asyncio.windows_events import NULL

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree(object):

	def __init__(self): # Initializing the BST. Root points to None.
		self.root = None

	# HELPER FUNCTIONS

	# This function is O(n)
	def append_in_order(self,tree,in_order_list):
		if tree == None:
			return
		self.append_in_order(tree.left,in_order_list)
		in_order_list.append(tree.value)
		self.append_in_order(tree.right,in_order_list)

	# This function is O(n)
	def append_pre_order(self,tree,pre_order_list):
		if tree == None:
			return
		pre_order_list.append(tree.value)
		self.append_pre_order(tree.left,pre_order_list)
		self.append_pre_order(tree.right,pre_order_list)

	# This function is O(n)
	def append_post_order(self,tree,post_order_list):
		if tree == None:
			return
		self.append_post_order(tree.left,post_order_list)
		self.append_post_order(tree.right,post_order_list)
		post_order_list.append(tree.value)

	# This function is O(h) which could be O(n) in worst case
	def recursive_insert(self,root,val,flag):
		if root is None:
			return Node(val)
		else:
			if root.value == val:
				flag = False
				return Node(val)
			elif root.value < val:
				root.right = self.recursive_insert(root.right,val,flag)
			else:
				root.left = self.recursive_insert(root.left,val,flag)
			return root

	# This function is O(h) which could be O(n) in worst case
	def find(self,tree,val):
		if tree is None:
			return False
		else:
			if tree.value == val:
				return tree
			elif val<tree.value:
				return self.find(tree.left,val)
			else:
				return self.find(tree.right,val)

	# This function is O(n)
	def height(self,tree):
		if tree is None:
			return 0
		else:
			return 1 + max(self.height(tree.left), self.height(tree.right))

	# This function is O(h) which could be O(n) in worst case
	def path(self,tree,val,list):
		if tree is None:
			return list
		else:
			list.append(tree.value)
			if tree.value == val:
				return list
			elif val<tree.value:
				return self.path(tree.left,val,list)
			else:
				return self.path(tree.right,val,list)

	# This function is O(h) which could be O(n) in worst case
	def leftmost(self,tree):
		result = tree
		while(result.left != None):
			result = result.left
		return result

	# This function is O(h) which could be O(n) in worst case
	def delete_node(self,tree,key):
		if tree is None:
			return tree
		else:
			if key<tree.value:
				tree.left = self.delete_node(tree.left,key)

			elif key>tree.value:
				tree.right = self.delete_node(tree.right,key)

			else:
				if tree.left is None:
					x = tree.right
					tree = None
					return x
				elif tree.right is None:
					x = tree.left
					tree = None
					return x
				else:
					x = self.leftmost(tree.right)
					tree.value = x.value
					tree.right = self.delete_node(tree.right,x.value)
					
			return tree

	# Part 1 starts here

	# This function is O(n)
	def in_order(self):
		in_order_list = []
		self.append_in_order(self.root,in_order_list)
		return in_order_list
		
	# This function is O(n)
	def pre_order(self):
		pre_order_list = []
		self.append_pre_order(self.root,pre_order_list)
		return pre_order_list
		
	# This function is O(n)
	def post_order(self):
		post_order_list = []
		self.append_post_order(self.root,post_order_list)
		return post_order_list

	# This function is O(h), where h is the height of the tree, which could be O(n) in worst case
	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			flag = True
			self.recursive_insert(self.root,val,flag)
			if flag == False:
				return False

	# This function is O(n)
	def get_node(self, key): 
		x = self.find(self.root,key)
		return x
		
	# This function is O(n)
	def find_node(self, key):
		result = self.find(self.root,key)
		if result != False:
			return True
		return result
		
	# This function is O(n)
	def get_children(self, key):
		result = self.find(self.root,key)
		return result.left, result.right
	
	# This function is O(n)
	def update_node(self, key, val):
		result = self.get_node(key)
		if result.left.value > val or result.right.value < val:
			return False
		else:
			result.value = val
	
	# This function is O(n)
	def get_height(self):
		return self.height(self.root)
		
	# This function is O(n)
	def get_path(self, key):
		list = []
		return self.path(self.root,key,list)
		
	# This function is O(n)
	def avg_diff(self):
		left_list = []
		self.append_in_order(self.root.left,left_list)
		avg_left = sum(left_list)/len(left_list)
		right_list = []
		self.append_in_order(self.root.right,right_list)
		avg_right = sum(right_list)/len(right_list)
		diff = abs(avg_left - avg_right)
		return diff

	# This function is O(n)
	def delete(self, key):
		return self.delete_node(self.root,key)

	# This function is O(n) 
	def delete_leaf(self, key):
		x = self.get_node(key)
		if x.left != None or x.right != None:
			return False
		else:
			self.delete(key)

	# This function is O(n) 
	def delete_leaves(self):
		list = self.in_order()
		for key in list:
			self.delete_leaf(key)

# Testing Area ---

# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
def main():
	pass

    # Create an object here to test the functions.

# Comment out the line below before running your test files.
#main()