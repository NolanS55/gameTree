#    Main Author(s): Nolan Smith
#    Main Reviewer(s): Christian Ricci

from queueSelf import Queue
#takes in grid to check for overflowing numbers, returns tuple of overflowing positions in said grid
def get_overflow_list(grid):
	rows = len(grid)
	cols = len(grid[0])

	#Defines where to look for the neighbors of each element
	neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	overflow_list = []	
	#goes through each element in the grid
	for row in range(rows):
		for col in range(cols):
			cell = grid[row][col]
			neighborNum = 0
			#checks the neighbors of each element
			for r, c in neighbors:
				newRow, newCol = row + r, col + c
				#makes sure the neighbors are valid
				if (0 <= newRow and newRow < rows) and (0 <= newCol and newCol < cols):
					neighborNum += 1
			#gets the absolute value of sell and checks if it is valid for overflowing
			if abs(cell) >= neighborNum:
				overflow_list.append((row, col))
	if overflow_list == []:
		return None
	return overflow_list 

#Takes in a grid and a queue to store copy's of the grid, returns number of grids created
def overflow(grid, a_queue):
	#Deep copy function to add to enque
	def deepCopy(source):
		rows = len(source)
		cols = len(source[0])
		tmpGrd = [[0 for x in range(cols)] for y in range(rows)] 
		for row in range(rows):
			for col in range(cols):
				tmpGrd[row][col] = source[row][col]
		return tmpGrd
	def sign(num):
		if num * -1 > 0:
			return "-"
		return "+"
	rows = len(grid)
	cols = len(grid[0])
	#Gets all overflowed cells
	tmpGrd = deepCopy(grid)


	overflowedCells = get_overflow_list(grid)
	#breaks when no more are overflowing
	if overflowedCells == None:
		gridCount = overflow.count
		overflow.count = 0
		return gridCount
	overflow.count += 1


	
	
	#ERROR IS CAUSED BY ROW COL OVERRIDDEN AND SETTING A CHANGED CELL TO ZERO WHEN IT SHOULD BE 1

	#runs through each overflowing cell
	for row, col in overflowedCells:
		#defines the neighbors of each cell
		neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
		#runs through the position of all neighbors to our main cell
		for r, c in neighbors:
			#makes sure the neighbor is a valid position on grid
			if (0 <= r and r < rows) and (0 <= c and c < cols):
				#checks if the original number is negative
				if grid[row][col] < 0:
					#checks if neighbor number is positive and coverts it to negative if it is
					if grid[r][c] > 0:
						grid[r][c] *= -1
					grid[r][c] -= 1	
				else:
					#checks if neighbor number is negative and converts it to positive
					if grid[r][c] < 0:
						grid[r][c] = abs(grid[r][c])
					grid[r][c] += 1
	#sets original overflowing number to correct values
	for row,col in overflowedCells:
		if tmpGrd[row][col] != grid[row][col]:
			if(tmpGrd[row][col] < grid[row][col]):
				grid[row][col] -= tmpGrd[row][col]
			else:
				grid[row][col] += tmpGrd[row][col]
		else:
			grid[row][col] = 0
	signs = set()
	
	for row in grid:
		for cell in row:
			signs.add(sign(cell))
    
	if len(signs) == 1:
		a_queue.enqueue(deepCopy(grid))
		gridCount = overflow.count
		overflow.count = 0
		return gridCount	

	a_queue.enqueue(deepCopy(grid))
	return overflow(grid,a_queue)
overflow.count = 0