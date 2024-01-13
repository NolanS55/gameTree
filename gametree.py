# Main Authors: Christian Ricci, Nolan Smith
# Main Reviewer: Christian Ricci, Nolan Smith

from queueSelf import Queue
from overflow import overflow

# This function duplicates and returns the board.
def copy_board(board):

        current_board = []
        height = len(board)

        for i in range(height):

            current_board.append(board[i].copy())

        return current_board

# This function returns the score for the board.
def evaluate_board (board, player):

    def cellValue(cell_value):

        if cell_value == 0:

            return 0  # Empty cell has no score

        elif cell_value > 0:

            return 1  # Player's pieces contribute positively

        elif cell_value < 0:

            return -1  # Opponent's pieces contribute negatively

    player1Score = 0
    player2Score = 0

    for i in range(len(board)):

        for j in range(len(board[0])):

            if cellValue(board[i][j]) == -1:

                player2Score += 1

            elif cellValue(board[i][j]) == 1:

                player1Score += 1
    
    # Player 1 or Player 2 has won the game.
    if (player1Score > 0 and player2Score == 0 and player == 1) or (player2Score > 0 and player1Score == 0 and player == -1):

        return 10

    # Player 1 or Player 2 has lost the game.
    elif (player1Score > 0 and player2Score == 0 and player == -1) or (player2Score > 0 and player1Score == 0 and player == 1):

        return 0

    return 5
    
class GameTree:

    class Node:

        # This init function will initialize the node.
        def __init__(self, board, depth, player, tree_height = 4):

            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []

            if self.depth < self.tree_height:

                self.generateChildren()
        
        # This function creates children for each node representing the placement of a piece.
        def generateChildren(self):
            
            queue = Queue()

            for i in range(len(self.board)):

                for j in range(len(self.board)):

                    if self.player == 1 and self.board[i][j] > 0:

                        board = copy_board(self.board)
                        board[i][j] = board[i][j] + 1
                        overflow(board, queue)

                        if evaluate_board(board, self.player) != 0:

                            child = GameTree.Node(board, self.depth + 1, -1, self.tree_height)
                            self.children.append(((i, j), child))

                    if self.player == -1 and self.board[i][j] < 0:

                        board = copy_board(self.board)
                        board[i][j] = board[i][j] - 1
                        overflow(board, queue)

                        if evaluate_board(board, self.player) != 0:
                                
                            child = GameTree.Node(board, self.depth + 1, 1, self.tree_height)
                            self.children.append(((i, j), child))

        # This functions returns the score of the node. 
        # For any leaf node, the board is evaluated using the evaluate_board function.
        # For any inner node, the minimax algorithm determines the score for the node.self.clear_tree()
        def scoreNode(self, player):

            if len(self.children) == 0:

                return evaluate_board(self.board, player)

            if self.player == 1:

                return max(child[1].scoreNode(player) for child in self.children)

            elif self.player == -1:

                return min(child[1].scoreNode(player) for child in self.children)

    # This init function will build the game tree to a height of tree_height.
    def __init__(self, board, player, tree_height = 4):

        self.board = copy_board(board)
        self.player = player
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, self.player, self.tree_height)

    # This function gets (row,col) which is the position of the choice from the tree.
    def get_move(self):
        
        bestScore = 0
        bestMove = None

        for child in self.root.children:

            childScore = child[1].scoreNode(self.player)
            
            if childScore > bestScore:

                bestScore = childScore
                bestMove = child[0]
                
                self.clear_tree()
                
        return bestMove

   # This function destroys the game tree by unlinking all nodes in order to allow the garbage collector to work on clearing the memory.
    def clear_tree(self):
        self.clear_node(self.root)
        self.root = None  

    def clear_node(self, node):
        if node:
            #clear each child with recursion
            for child in node.children:
                self.clear_node(child[1])#make sure we are clearing the first child and not the position
        node.children = []
        node = None 
