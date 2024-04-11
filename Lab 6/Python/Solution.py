class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        visited = [False] * numCourses
        recursion_stack = [False] * numCourses
        for i in range(numCourses):
            if not visited[i] and self.is_cyclic(graph, i, visited, recursion_stack):
                return False 
        return True

    def is_cyclic(self, graph: List[List[int]], node: int, visited: List[bool], recursion_stack: List[bool]) -> bool:
        if recursion_stack[node]:
            return True  
        if visited[node]:
            return False
        visited[node] = True
        recursion_stack[node] = True
        for neighbor in graph[node]:
            if self.is_cyclic(graph, neighbor, visited, recursion_stack):
                return True
        recursion_stack[node] = False
        return False

solution = Solution()
numCourses1 = 2
prerequisites1 = [[1, 0]]
print("Test Case 1:", solution.canFinish(numCourses1, prerequisites1))  # Output: True

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print("Test Case 2:", solution.canFinish(numCourses2, prerequisites2))  # Output: False
