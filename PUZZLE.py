from collections import deque
class Solution:
    def solve(self, board):
        start = tuple(sum(board, []))  # Flatten the 2D board into a 1D tuple
        goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        if start == goal:
            return 0
        moves = {
            1: (0, 1), -1: (0, -1),  # Horizontal moves
            3: (1, 0), -3: (-1, 0)  # Vertical moves
        }
        queue = deque([(start, 0)])  # (current state, depth)
        visited = set([start])
        while queue:
            state, depth = queue.popleft()
            blank_index = state.index(0)
            for shift, (row_delta, col_delta) in moves.items():
                new_index = blank_index + shift
                if (
                    0 <= new_index < 9  # Within bounds of the 1D array
                    and (
                        blank_index // 3 + row_delta == new_index // 3  # Same row
                        or blank_index % 3 + col_delta == new_index % 3  # Same column
                    )
                ):
                    new_state = list(state)
                    new_state[blank_index], new_state[new_index] = (
                        new_state[new_index],
                        new_state[blank_index],
                    )
                    new_state = tuple(new_state)         
                    if new_state == goal:
                        return depth + 1      
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, depth + 1))
        return -1  
ob = Solution()
matrix = [[3, 1, 2], [4, 7, 5], [6, 8, 0]]
print(ob.solve(matrix))
