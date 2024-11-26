def water_jug_dfs(c1, c2, target):
    visited, path = set(), []

    def dfs(j1, j2):
        if (j1, j2) in visited or j1 > c1 or j2 > c2:
            return False
        visited.add((j1, j2))
        path.append((j1, j2))
        if (j1, j2) == (0, target):
            return True
        if dfs(c1, j2):
            return True
        if dfs(j1, c2): 
            return True
        if dfs(0, j2): 
            return True
        if dfs(j1, 0): 
            return True
        if dfs(max(0, j1 - (c2 - j2)), min(c2, j1 + j2)):
            return True
        if dfs(min(c1, j1 + j2), max(0, j2 - (c1 - j1))):
            return True
        return False

    dfs(0, 0)
    return path

capacity1, capacity2, target = 4, 3, 2
solution = water_jug_dfs(capacity1, capacity2, target)
for step in solution:
    print(step)
