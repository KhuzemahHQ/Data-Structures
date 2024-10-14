# Assignment 2-Part 2
# AVL Trees


class TreeNode(object):
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None
		self.h = 1



class AVLTree(object):
	# Helper Functions
	# This function is O(h) = O(logn)
	def leftmost(self,tree):
		result = tree
		while(result.l != None):
			result = result.l
		return result

	# This function is O(n)
	def search(self,root,list_at_level,level_height):
		if root is None:
			return
		if self.get_height(root) == level_height:
			list_at_level.append(root.value)
		self.search(root.l,list_at_level,level_height)
		self.search(root.r,list_at_level,level_height)
		

	# Part 2 starts here
	# This function is O(h) = O(logn)
	def insert(self, root,key):
		if root is None:
			return TreeNode(key)
		elif key < root.value:
			root.l = self.insert(root.l, key)
		else:
			root.r = self.insert(root.r, key)

		root.h = 1 + max(self.get_height(root.l), self.get_height(root.r))
		# Four different kinds of rotations for rebalancing:
		balance = self.get_bal(root)
		if balance < -1 and key > root.r.value:
			return self.l_rotate(root)
		if balance > 1 and key < root.l.value:
			return self.r_rotate(root)
		if balance > 1 and key > root.l.value:
			root.l = self.l_rotate(root.l)
			return self.r_rotate(root)
		if balance < -1 and key < root.r.value:
			root.r = self.r_rotate(root.r)
			return self.l_rotate(root)
		return root
	
	# This function is O(1)
	def l_rotate(self, z):
		if z is None:
			return None

		new_parent = z.r
		temp = new_parent.l
		new_parent.l = z
		z.r = temp

		z.h = 1 + max(self.get_height(z.l),self.get_height(z.r))
		new_parent.h = 1 + max(self.get_height(new_parent.l),self.get_height(new_parent.r))
		return new_parent
	
	# This function is O(1)
	def r_rotate(self, z):
		if z is None:
			return None

		new_parent = z.l
		temp = new_parent.r
		new_parent.r = z
		z.l = temp

		z.h = 1 + max(self.get_height(z.l),self.get_height(z.r))
		new_parent.h = 1 + max(self.get_height(new_parent.l),self.get_height(new_parent.r))
		return new_parent

	# This function is O(1)
	def get_height(self,root):
		if root is None:
			return 0
		else:
			return root.h 

	# This function is O(1)
	def get_bal(self,root):
		if root is None:
			return None
		else:
			return self.get_height(root.l) - self.get_height(root.r)


# You are requied return the the value of the root in a list after
# If Root is not Found then you are required to return None

	# This function is O(h) = O(logn)
	def delete_node(self, root,node_to_be_deleted):
		if root is None:
			return root
		elif root.value < node_to_be_deleted:
			root.r = self.delete_node(root.r,node_to_be_deleted)
		elif root.value > node_to_be_deleted:
			root.l = self.delete_node(root.l,node_to_be_deleted)
		else:
			if root.l is None:
				temp = root.r
				root = None
				return temp
			elif root.r is None:
				temp = root.l
				root = None
				return temp
			x = self.leftmost(root.r)
			root.value = x.value
			root.r = self.delete_node(root.r,x.value)

		if root is None:
			return root

		# Four different kinds of rotations for rebalancing:
		balance = self.get_bal(root)
		if balance < -1 and root.value  > root.r.value:
			return self.l_rotate(root)
		if balance > 1 and root.value < root.l.value:
			return self.r_rotate(root)
		if balance > 1 and root.value  > root.l.value:
			root.l = self.l_rotate(root.l)
			return self.r_rotate(root)
		if balance < -1 and root.value < root.r.value:
			root.r = self.r_rotate(root.r)
			return self.l_rotate(root)
		return root

	# This function is O(logn)
	def update_node(self,root, new_value_of_node,old_value_of_node):
	
		if root is None:
			return None

		if root.value == old_value_of_node:
			if root.r is None and root.l is None:
				root.value = new_value_of_node
			elif root.r.value > new_value_of_node and root.l.value < new_value_of_node:
				root.value = new_value_of_node
			return root
		elif root.value < old_value_of_node:
			return self.update_node(root.r,new_value_of_node,old_value_of_node)
		else:
			return self.update_node(root.l,new_value_of_node,old_value_of_node)

	# This function is O(nlogn)
	def delete_all_nodes_at_given_height(self,root,level):
		tree_height = self.get_height(root)
		list_at_level = []
		level_height = tree_height - level
		self.search(root,list_at_level,level_height)

		for element in list_at_level:
			self.delete_node(root,element)


# Testing Area ---

# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
# Create an object here to test the functions.

if __name__ == "__main__":
    pass


	
