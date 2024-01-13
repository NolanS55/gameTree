class Queue:
	# This function initializes the Queue class data members. Gets passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.
	def __init__(self, cap = 10):

		self.cap = cap
		self.queue = [None] * cap
		self.front = 0
		self.back = 0
		self.numOfElements = 0

	# This function returns the capacity of the Queue.
	# Runtime Requirement: O(1).
	def capacity(self):
		
		return self.cap

	# This function adds data to the "back" of the Queue.
	# If number of items exceeds the current capacity, a resizing operation will need to take place. Resizing always doubles the current capacity of the array.
	# This function does not return anything.
	# Runtime Requirement: O(1) when no resizing occurs, O(n) when resizing occurs.
	def enqueue(self, data):
		
		if self.numOfElements == self.cap:

			tempQueue = [None] * (self.cap * 2)

			if self.back != self.cap:

				for i in range(self.cap):
					
					if self.front == self.cap:

						self.front = 0
						tempQueue[i] = self.queue[self.front]
						self.front = self.front + 1
					
					else:

						tempQueue[i] = self.queue[self.front]
						self.front = self.front + 1

				self.queue = tempQueue
				self.front = 0
				self.back = self.cap

				self.cap = self.cap * 2

			else:

				for i in range(self.cap):

					tempQueue[i] = self.queue[i]

				self.cap = self.cap * 2
				self.queue = tempQueue

		elif self.back == self.cap:

			self.back = 0
	
		self.queue[self.back] = data
		self.back = self.back + 1
		self.numOfElements = self.numOfElements + 1

	# This function removes the oldest value from the Queue (the value at the "front" of the Queue).
	# If the function is called on an empty Queue, raise the IndexError with the statement "raise IndexError('dequeue() used on empty queue')". 
	# This function returns the value removed.
	# Runtime Requirement: O(1).
	def dequeue(self):
		
		if self.is_empty():

			raise IndexError('dequeue() used on empty queue')
		
		else:

			value = self.queue[self.front]
			self.queue[self.front] = None
			self.front = self.front + 1
			self.numOfElements = self.numOfElements - 1

			return value

	# This function returns the the oldest value (value at "front") from the Queue without removing it. 
	# This function returns None if Queue is empty.
	# Runtime Requirement: O(1).
	def get_front(self):

		if self.numOfElements == 0:

			return None
		
		else:
		
			return self.queue[self.front]

	# This function returns True if Queue is empty, False otherwise. 
	# Runtime Requirement: O(1).
	def is_empty(self):
		
		if self.numOfElements == 0:

			return True
		
		else:

			return False

	# This function returns the number of values in the Queue. 
	# Runtime Requirement: O(1).
	def __len__(self):
		
		return self.numOfElements

