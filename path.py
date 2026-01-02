# 6. Simple Path Validator 
# Represent a small map as a dictionary like {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": 
# {"B", "C"}}. Ask the user to input a path, e.g., ["A", "C", "D"]. Check if each consecutive step is 
# connected and print "Valid path" or "Invalid path".
# Map represented as a dictionary
graph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D"},
    "D": {"B", "C"}
}
user_input = input("Enter path (like A C D): ").split()
def validate_path(path):
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        if next_node not in graph[current_node]:
            return False
    return True

if validate_path(user_input):
    print("Valid path")
else:
    print("Invalid path")