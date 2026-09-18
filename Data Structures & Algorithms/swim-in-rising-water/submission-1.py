class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #edge cases:
        #grid = [],

        length = len(grid)

        def get_neighboors(i,j):
            neighboors = []
            neighboors.append((i,j))
            if i < length -1:
                neighboors.append((i+1,j))
            if j < length -1:
                neighboors.append((i,j+1))
            if i > 0:
                neighboors.append((i-1,j))
            if j > 0:
                neighboors.append((i,j-1))
            return neighboors


        def search(square):
            import heapq

            init_i, init_j = square
            heap = [(grid[init_i][init_j], init_i, init_j)]
            visited = {(init_i, init_j)}

            while heap:
                t, i, j = heapq.heappop(heap)
                
                if i == length -1 and j == length -1:
                    return t
                
                for n_i, n_j in get_neighboors(i,j):
                    if (n_i,n_j) not in visited:
                        visited.add((n_i,n_j))
                        heapq.heappush(heap, (max(t, grid[n_i][n_j]) , n_i, n_j ))
            return 0
        
        return search((0,0))

'''
Input: grid = [[0,1],[2,3]] Output: 3
length = 2
(0,0,0) -> neighboors = [(1,0),(0,1)] visited = [(0,0)] queue = [(0,0,1),(0,1,1)]
(0,0,1) -> neighboors = [(1,0),(0,1)] visited = [(0,1)] queue = [(0,1,1),(1,0,2)]
(0,1,1) -> neighboors = [(0,0),(1,1)] visited = [(0,1),(1,0)] queue = [(1,0,2)]
'''
