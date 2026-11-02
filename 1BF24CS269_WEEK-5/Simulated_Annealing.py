
import random
import math

# Calculate number of attacking queen pairs
def calculate_cost(board):
    cost = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


# Display chess board
def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Simulated Annealing algorithm
def simulated_annealing():
    n = 8

    # Generate random initial board
    board = [random.randint(0, n - 1) for _ in range(n)]
    current_cost = calculate_cost(board)

    temperature = 100
    cooling_rate = 0.99

    while temperature > 0.01:

        # Check goal state
        if current_cost == 0:
            print("Solution Found!")
            print("Final Board:", board)
            print("Cost:", current_cost)
            print_board(board)
            return

        # Generate random neighboring state
        neighbor = board[:]

        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)

        while row == neighbor[col]:
            row = random.randint(0, n - 1)

        neighbor[col] = row

        new_cost = calculate_cost(neighbor)

        # Calculate cost difference
        delta = new_cost - current_cost

        # Accept or reject new state
        if delta < 0:
            board = neighbor
            current_cost = new_cost

        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                board = neighbor
                current_cost = new_cost

        # Reduce temperature
        temperature = temperature * cooling_rate

    # Final check
    if current_cost == 0:
        print("Solution Found!")
        print("Final Board:", board)
        print_board(board)
    else:
        print("Solution Not Found!")


# Main function
simulated_annealing()
