import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                int left = i + 1, right = n - 1, target = -nums[i];
                while (left < right) {
                    int sum = nums[left] + nums[right];
                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) left++;
                    else right--;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        ThreeSum solution = new ThreeSum();
        int[] nums1 = {0, 1, 1};
        System.out.println("Test Case 1: " + solution.threeSum(nums1)); // Output: []

        int[] nums2 = {-5, 0, 5, 10, -10, 0};
        System.out.println("Test Case 2: " + solution.threeSum(nums2)); // Output: [[-10, 0, 10], [-5, 0, 5]]
    }
}
