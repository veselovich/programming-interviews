import time
from memory_profiler import profile
import random


def initialize_hash_values():
    piece_types = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    colors = ['white', 'black']
    board_size = 8 # 8x8 chess board

    hash_values = {}
    for row in range(board_size):
        for col in range(board_size):
            for piece in piece_types:
                for color in colors:
                    hash_values[(piece, color, row, col)] = random.getrandbits(64)

    return hash_values

def compute_initial_hash(board, hash_values):
    board_hash = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece:  # Check if the square is not empty
                # piece is a tuple (type, color)
                piece_type, piece_color = piece
                board_hash ^= hash_values[(piece_type, piece_color, row, col)]

    return board_hash

def update_hash(board, board_hash, move, hash_values):
    from_square, to_square = move
    moving_piece = board[from_square[0]][from_square[1]]
    captured_piece = board[to_square[0]][to_square[1]]

    # Check if the moving piece is not None
    if moving_piece:
        # XOR out the moving piece from its original square
        board_hash ^= hash_values[(moving_piece[0], moving_piece[1], from_square[0], from_square[1])]
        # XOR in the moving piece on its new square
        board_hash ^= hash_values[(moving_piece[0], moving_piece[1], to_square[0], to_square[1])]

    # Handle captured piece, if any and not None
    if captured_piece:
        board_hash ^= hash_values[(captured_piece[0], captured_piece[1], to_square[0], to_square[1])]

    return board_hash


def main():
    start_time = time.time()

    #test case

    # Define the initial board
    board = [
        [('rook', 'white'), ('knight', 'white'), ('bishop', 'white'), ('queen', 'white'), ('king', 'white'), ('bishop', 'white'), ('knight', 'white'), ('rook', 'white')],
        [('pawn', 'white')] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [('pawn', 'black')] * 8,
        [('rook', 'black'), ('knight', 'black'), ('bishop', 'black'), ('queen', 'black'), ('king', 'black'), ('bishop', 'black'), ('knight', 'black'), ('rook', 'black')]
    ]

    # Initialize hash values and compute initial board hash
    hash_values = initialize_hash_values()
    board_hash = compute_initial_hash(board, hash_values)

    print("Initial hash", board_hash)

    # Define the move E2 to E4
    from_square = (6, 4)  # E2
    to_square = (4, 4)    # E4
    move = (from_square, to_square)

    # Then update the hash
    board_hash = update_hash(board, board_hash, move, hash_values)

    board[4][4] = board[6][4]
    board[6][4] = None 

    print("Updated hash after E2 to E4:", board_hash)

    # Define the move E2 to E4
    from_square = (4, 4)  # E2
    to_square = (6, 4)    # E4
    move = (from_square, to_square)

    # Then update the hash
    board_hash = update_hash(board, board_hash, move, hash_values)

    board[6][4] = board[4][4]
    board[4][4] = None 

    print("Updated hash after E4 to E2:", board_hash)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()