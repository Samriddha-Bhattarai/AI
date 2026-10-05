# 8-Puzzle using Iterative Deepening Search (IDS)

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Function to print the puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Generate possible moves
def get_neighbors(state):

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank and tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# Depth Limited Search
def depth_limited_search(state, depth, path, visited):

    # Goal test
    if state == GOAL:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    visited.add(state)

    # Generate next states
    for next_state in get_neighbors(state):

        if next_state not in visited:

            result = depth_limited_search(
                next_state,
                depth - 1,
                path + [next_state],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


# Iterative Deepening Search
def ids(start, max_depth=30):

    for depth in range(max_depth + 1):

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            start,
            depth,
            [start],
            visited
        )

        if result is not None:
            return result

    return None


# Display solution
def display_solution(path):

    if path is None:

        print("\nNo solution found.")
        return

    print("\nIDS Solution")
    print("--------------------")

    print("Number of moves:", len(path) - 1)
    print()

    for i, state in enumerate(path):

        print("Step", i)
        print_puzzle(state)


# Main Program

print("================================")
print("       8-PUZZLE USING IDS")
print("================================")

print("\nEnter the initial state.")
print("Use 0 for the blank space.")

values = list(
    map(int, input("Enter 9 numbers: ").split())
)

# Validate input
if len(values) != 9 or set(values) != set(range(9)):

    print("\nInvalid input!")
    print("Enter numbers 0 to 8 exactly once.")

else:

    start = tuple(values)

    print("\nInitial State:")
    print_puzzle(start)

    print("Goal State:")
    print_puzzle(GOAL)

    print("\nRunning IDS...")

    solution = ids(start)

    display_solution(solution)