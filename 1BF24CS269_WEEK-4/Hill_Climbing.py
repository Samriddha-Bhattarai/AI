
# Hill Climbing Algorithm for 4 Queens

import random

# Calculate cost
def calculate_cost(board):
    cost = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


# Display board
def print_board(board):
    for row in range(4):
        for col in range(4):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Hill Climbing
def hill_climbing():

    board = list(map(int, input("Enter initial state: ").split()))

    if len(board) != 4 or any(x < 0 or x > 3 for x in board):
        print("Invalid input!")
        return

    step = 1

    while True:

        current_cost = calculate_cost(board)

        print("\nStep:", step)
        print("Current State:", board)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("\nSolution Found!")
            break

        best_board = board[:]
        best_cost = current_cost

        print("\nNeighboring States:")

        for col in range(4):
            for row in range(4):

                neighbor = board[:]
                neighbor[col] = row

                cost = calculate_cost(neighbor)

                print(neighbor, "Cost:", cost)

                if cost < best_cost:
                    best_cost = cost
                    best_board = neighbor

        if best_cost >= current_cost:
            print("\nLocal Minimum Reached!")
            print("Restarting with a new random state...")
            board = [random.randint(0, 3) for _ in range(4)]
        else:
            board = best_board
            print("\nBest Neighbor Selected:", board)
            print("New Cost:", best_cost)

        step += 1

    print("\nFinal State:", board)
    print("Final Cost:", calculate_cost(board))

    print("\nChess Board:")
    print_board(board)


hill_climbing()
