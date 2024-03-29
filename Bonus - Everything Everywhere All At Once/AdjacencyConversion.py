def adjacency_matrix_to_list(matrix):
    n = len(matrix)
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
                
    return adj_list

def main_matrix_to_adj_list():
    matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    print("Adjacency Matrix:", matrix)
    print("Adjacency List:", adjacency_matrix_to_list(matrix))

if __name__ == "__main__":
    main_matrix_to_adj_list()

# Output: Adjacency Matrix: [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    # Adjacency List: [[1, 2], [0], [0]]