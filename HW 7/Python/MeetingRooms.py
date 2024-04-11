class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end_times = []
        rooms = 0
        for start, end in intervals:
            if end_times and end_times[0] <= start:
                heapq.heappop(end_times)
            else:
                rooms += 1
            heapq.heappush(end_times, end)
        return rooms

solution = Solution()
intervals1 = [[0, 30], [5, 10], [15, 20]]
print("Test Case 1:", solution.minMeetingRooms(intervals1))  # Output: 2

intervals2 = [[0, 1], [1, 2], [2, 3]]
print("Test Case 2:", solution.minMeetingRooms(intervals2))  # Output: 1
