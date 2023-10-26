import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def is_goal(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_successors(node):
    successors = []
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move_names = ["Right", "Down", "Left", "Up"]

    blank_row, blank_col = get_blank_position(node.state)

    for move, move_name in zip(moves, move_names):
        new_row, new_col = blank_row + move[0], blank_col + move[1]

        if is_valid_position(new_row, new_col):
            new_state = [row[:] for row in node.state]  # Copy the state
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            successors.append((new_state, move_name))

    return successors

def is_valid_position(row, col):
    return 0 <= row < 3 and 0 <= col < 3


def heuristic(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                total_distance += 1
    return total_distance

def solve_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    open_list = []
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if is_goal(current_node.state):
            path = []
            while current_node.move:
                path.insert(0, (current_node.state, current_node.move))
                current_node = current_node.parent
            path.insert(0, (current_node.state, None))
            return path

        successors = generate_successors(current_node)
        for successor_state, move_name in successors:
            successor_node = PuzzleNode(successor_state, current_node, move_name, current_node.cost + 1)
            successor_node.cost = successor_node.cost + heuristic(successor_state)
            heapq.heappush(open_list, successor_node)

    return None

def print_puzzle(state):
    for row in state:
        print(" ".join(str(cell) for cell in row))

# Input your initial puzzle state
initial_state = []
for i in range(3):
    row = list(map(int, input(f"Enter row {i + 1} (separated by spaces): ").split()))
    initial_state.append(row)

solution = solve_puzzle(initial_state)

if solution:
    for step, (state, move) in enumerate(solution):
        print(f"Step {step + 1}:")
        if move:
            print(f"Move the blank tile {move}:")
        print_puzzle(state)
        print()
else:
    print("No solution found.")
