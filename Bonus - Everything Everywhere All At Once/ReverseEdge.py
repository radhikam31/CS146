def reverse_edges(graph):
    reversed_graph = [[] for _ in range(len(graph))]
    
    for i in range(len(graph)):
        for j in graph[i]:
            reversed_graph[j].append(i)
            
    return reversed_graph

def main_reverse_edges():
    graph = [[1, 2], [0], [0]]
    print("Original Graph:", graph)
    print("Reversed Graph:", reverse_edges(graph))

if __name__ == "__main__":
    main_reverse_edges()
