
class Node(object):
	def __init__(self, data="None", priority="None"):
		self.data = data
		self.priority = priority
		self.next = None



"""
Operations:
	push()
	pop()
	peek()
"""
class PriorityQueueLL(object):
	def __init__(self):
		self.head = None

	def push(self, data, priority):
		if self.head is None:
			new_node = Node(data, priority)
			self.head = new_node
			return True


		# The first element will not be checked the way our while is setup. 
		# need to manually check head accordingly

		new_node = Node(data, priority)

>>>>>>> master
		if priority >= self.head.priority:
				new_node.next = self.head
				self.head = new_node
				return True

		cur_node = self.head
		while cur_node.next:
			if priority >= cur_node.next.priority:
				# insert at current.next position
				new_node.next = cur_node.next
				cur_node.next = new_node
				return True
			cur_node = cur_node.next

		# If we get here, that means we reached end of list, 
		# which implies: new_node priority is < than all nodes in list
		# So insert at end of list. cur_node is last node right now. 
		cur_node.next = new_node
		

	def pop(self):
		"""
		: returns the highest priority node and remove from the queue, 
		: AKA remove and return head
		"""
		if self.head is None:
			return

		if self.head.next is None:
			temp = self.head
			self.head = None
			return temp
		else:
			temp = self.head
			self.head = self.head.next
			return temp

		return False
		

	def peek(self):
		pass

	def print_all(self):
		if self.head is None:
			return

		cur_node = self.head
		while cur_node:
			if cur_node.next is None:
				print(cur_node.data+"["+str(cur_node.priority)+"]")
			else:
				print(cur_node.data+"["+str(cur_node.priority)+"] -> ", end="")
			cur_node = cur_node.next




# main stuff
pq = PriorityQueueLL()

pq.push("C", 3)
pq.push("A", 5)
pq.push("E", 1)
pq.push("B", 4)
pq.push("D", 2)

pq.print_all()
