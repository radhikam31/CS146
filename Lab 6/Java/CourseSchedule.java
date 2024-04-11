import java.util.*;

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] recursionStack = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] && isCyclic(graph, i, visited, recursionStack)) {
                return false; 
            }
        }
        return true;
    }

    private boolean isCyclic(List<List<Integer>> graph, int node, boolean[] visited, boolean[] recursionStack) {
        if (recursionStack[node]) return true; 
        if (visited[node]) return false;
        visited[node] = true;
        recursionStack[node] = true;
        for (int neighbor : graph.get(node)) {
            if (isCyclic(graph, neighbor, visited, recursionStack)) {
                return true;
            }
        }
        recursionStack[node] = false;
        return false;
    }

    public static void main(String[] args) {
        CourseSchedule solution = new CourseSchedule();
        int numCourses1 = 2;
        int[][] prerequisites1 = {{1, 0}};
        System.out.println("Test Case 1: " + solution.canFinish(numCourses1, prerequisites1)); // Output: true

        int numCourses2 = 2;
        int[][] prerequisites2 = {{1, 0}, {0, 1}};
        System.out.println("Test Case 2: " + solution.canFinish(numCourses2, prerequisites2)); // Output: false
    }
}
