import java.util.Arrays;
import java.util.PriorityQueue;

public class MeetingRooms {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> endTimes = new PriorityQueue<>();
        int rooms = 0;
        for (int[] interval : intervals) {
            if (!endTimes.isEmpty() && endTimes.peek() <= interval[0]) {
                endTimes.poll();
            } else {
                rooms++;
            }
            endTimes.offer(interval[1]);
        }
        return rooms;
    }

    public static void main(String[] args) {
        MeetingRooms solution = new MeetingRooms();
        int[][] intervals1 = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println("Test Case 1: " + solution.minMeetingRooms(intervals1)); // Output: 2

        int[][] intervals2 = {{0, 1}, {1, 2}, {2, 3}};
        System.out.println("Test Case 2: " + solution.minMeetingRooms(intervals2)); // Output: 1
    }
}
