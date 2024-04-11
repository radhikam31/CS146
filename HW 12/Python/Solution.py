class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = []
        for i, well_cost in enumerate(wells):
            edges.append([0, i + 1, well_cost])
        for pipe in pipes:
            edges.append(pipe)
        edges.sort(key=lambda x: x[2])

        parent = [-1] * (n + 1)
        total_cost = 0
        for edge in edges:
            u, v, cost = edge
            pu, pv = self.find(parent, u), self.find(parent, v)
            if pu != pv:
                parent[pu] = pv
                total_cost += cost
        return total_cost

    def find(self, parent: List[int], u: int) -> int:
        if parent[u] == -1:
            return u
        parent[u] = self.find(parent, parent[u])
        return parent[u]

solution = Solution()
n = 2
wells = [1, 1]
pipes = [[1, 2, 1], [1, 2, 2]]
print("Test Case 1:", solution.minCostToSupplyWater(n, wells, pipes))  # Output: 2
