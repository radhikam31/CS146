def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in adj_list[i]:
            matrix[i][j] = 1
            
    return matrix

def main_adj_list_to_matrix():
    adj_list = [[1, 2], [0, 2], [0, 1]]
    print("Adjacency List:", adj_list) #Adjacency List: [[1, 2], [0, 2], [0, 1]]
    print("Adjacency Matrix:", adjacency_list_to_matrix(adj_list)) #Adjacency Matrix: [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

if __name__ == "__main__":
    main_adj_list_to_matrix()
