def floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    
    def dfs(image, r, c, color, new_color):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color:
            return
        
        image[r][c] = new_color
        dfs(image, r+1, c, color, new_color)
        dfs(image, r-1, c, color, new_color)
        dfs(image, r, c+1, color, new_color)
        dfs(image, r, c-1, color, new_color)
    
    dfs(image, sr, sc, image[sr][sc], color)
    return image
