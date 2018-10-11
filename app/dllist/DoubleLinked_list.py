class Item:
	def __init__(self, elem):
		self.elem = elem
		self.next_item = None
		self.prev_item = None
		


class DoubleLinkedList:
	def __init__(self):
		self.head = None


	def push(self,elem):
		if self.head is None:
			new_node = Item(elem)
			new_node.prev_item = None
			self.head = new_node
		else:
			new_node = Item(elem)
			cur = self.head
			while cur.next_item:
				cur = cur.next_item
			cur.next_item = new_node
			new_node.prev_item = cur
			new_node.next_item = None


	def pop(self):
		cur = self.head
		if cur is None:
			return('empty DoubleLinked')
		elif cur.next_item is None:
			self.head = None
		else:
			while cur.next_item != None:
				cur = cur.next_item
			old_tail = cur
			old_tail.prev_item.next_item = None
			old_tail.prev_item = self.head


	def unshift(self,elem):#tested
		if self.head is None:
			new_node = Item(elem)
			new_node.prev_item = None
			new_node.next_item = None
			self.head = new_node
		else:
			old_head = self.head
			new_node = Item(elem)
			new_node.prev_item = None
			new_node.next_item = old_head
			old_head.prev_item = new_node
			self.head = new_node


	def shift(self):#tested 
		if self.head is None:
			return('empty DoubleLinked')
		elif self.head.next_item is None:
			self.head = None
		else:
			cur = self.head
			cur.next_item.prev_item =  None
			self.head = cur.next_item


	def len(self):#tested
		i = 0
		cur = self.head
		if cur is None:
			return(i)
		else:
			while cur:
				i+=1
				cur = cur.next_item
			return(i)


	def delete(self,elem):#tested
		cur = self.head
		while cur.elem != elem:
			cur = cur.next_item
		if (cur == self.head):
			self.shift()
		elif(cur.next_item is None):
			self.pop()
		else:
			cur.prev_item.next_item = cur.next_item
			cur.next_item.prev_item = cur.prev_item


	def contains(self,elem):#tested
		cur = self.head
		i = False
		if cur is None:
			return(False)
		else:
			while cur.next_item != None:
				if (cur.elem == elem):
					i = True
					break
				else:
					pass
				cur = cur.next_item
			return(True)

	def first(self):#tested
		if self.head is None:
			return('empty DoubleLinked')
		else:
			return(self.head.elem)


	def last(self):#tested
		if self.head is None:
			return('empty DoubleLinked')
		else:
			cur = self.head
			while cur.next_item != None:
				cur = cur.next_item
			return(cur.elem)


	def print_list(self):
		cur = self.head
		if cur is None:
			print("List is empty")
		while cur:
			print(cur.elem)
			cur = cur.next_item


	def dl_to_list(self):
		cur = self.head
		tmp_list = []
		if cur is None:
			return(tmp_list)
		else:
			while cur != None:
				tmp_list.append(cur.elem)
				cur = cur.next_item
			return(tmp_list)









