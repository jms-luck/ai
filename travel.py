import itertools

def tsp(dist):
    min_dist = float('inf')
    best_path = []
    # Generate all permutations of the cities (excluding the starting city, which is assumed to be 0)
    for path in itertools.permutations(range(1, len(dist))):
        # Create a full path that starts and ends at the starting city (0)
        full_path = [0] + list(path) + [0]
        dist_sum = sum(dist[full_path[i]][full_path[i + 1]] for i in range(len(full_path) - 1))
        if dist_sum < min_dist:
            min_dist = dist_sum
            best_path = full_path
            
    return best_path, min_dist

# Distance matrix representing the distances between cities
dist = [[0, 10, 15, 20], 
        [10, 0, 35, 25], 
        [15, 35, 0, 30], 
        [20, 25, 30, 0]]

# Find the best path and minimum distance
best_path, min_dist = tsp(dist)

# Print the results
print("Best path:", best_path)
print("Minimum distance:", min_dist)
