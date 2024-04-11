import java.util.*;

public class MinCostToSupplyWater {
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            edges.add(new int[]{0, i + 1, wells[i]});
        }
        for (int[] pipe : pipes) {
            edges.add(pipe);
        }
        edges.sort(Comparator.comparingInt(a -> a[2]));

        int[] parent = new int[n + 1];
        Arrays.fill(parent, -1);
        int totalCost = 0;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], cost = edge[2];
            int pu = find(parent, u), pv = find(parent, v);
            if (pu != pv) {
                parent[pu] = pv;
                totalCost += cost;
            }
        }
        return totalCost;
    }

    private int find(int[] parent, int u) {
        if (parent[u] == -1) return u;
        return parent[u] = find(parent, parent[u]);
    }

    public static void main(String[] args) {
        MinCostToSupplyWater solution = new MinCostToSupplyWater();
        int n = 2;
        int[] wells = {1, 1};
        int[][] pipes = {{1, 2, 1}, {1, 2, 2}};
        System.out.println("Test Case 1: " + solution.minCostToSupplyWater(n, wells, pipes)); // Output: 2
    }
}
