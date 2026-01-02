# Represent the map as a dictionary
map_graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}

# Ask the user to input a path
user_input = input("Enter a path as a list of nodes (e.g., A C D): ")
path = user_input.split()  # Convert input string into a list of nodes

# Initialize validity flag
is_valid = True

# Check consecutive steps in the path
for i in range(len(path) - 1):
    current_node = path[i]
    next_node = path[i + 1]
    # If next_node is not connected to current_node
    if next_node not in map_graph.get(current_node, {}):
        is_valid = False
        break

# Print result
if is_valid:
    print("Valid path")
else:
    print("Invalid path")