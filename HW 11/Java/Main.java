public class Main {
    public static void main(String[] args) {
        FloodFill floodFill = new FloodFill();
        int[][] image = {
            {1, 1, 1},
            {1, 1, 0},
            {1, 0, 1}
        };
        int sr = 1, sc = 1, color = 2;
        int[][] modifiedImage = floodFill.floodFill(image, sr, sc, color);
        for (int[] row : modifiedImage) {
            for (int pixel : row) {
                System.out.print(pixel + " ");
            }
            System.out.println();
        }
    }
}
