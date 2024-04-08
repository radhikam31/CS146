from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort_kahn(self):
        in_degree = {node: 0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in self.graph if in_degree[node] == 0])
        topological_order = []
        
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topological_order) != len(self.graph):
            print("Graph has a cycle")
            return []
        else:
            return topological_order
    
    def topological_sort_bfs(self):
        in_degree = {node: 0 for node in self.graph}
        for node in self.graph:
            for neighbor in self.graph[node]:
                in_degree[neighbor] += 1
        
        queue = deque([node for node in self.graph if in_degree[node] == 0])
        topological_order = []
        
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for neighbor in self.graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topological_order) != len(self.graph):
            print("Graph has a cycle")
            return []
        else:
            return topological_order
    
    def topological_sort_dfs(self):
        visited = set()
        stack = []
        
        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
        
        for node in self.graph:
            if node not in visited:
                dfs(node)
        
        return stack[::-1]

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("Kahn's Algorithm:", g.topological_sort_kahn())
print("BFS:", g.topological_sort_bfs())
print("DFS:", g.topological_sort_dfs())
