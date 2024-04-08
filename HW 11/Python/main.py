from floodfill import floodFill

def main():
    image = [[1,1,1],
             [1,1,0],
             [1,0,1]]
    sr, sc, color = 1, 1, 2
    modified_image = floodFill(image, sr, sc, color)
    print(modified_image) #output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

if __name__ == "__main__":
    main()
