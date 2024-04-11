class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                left, right = i + 1, n - 1
                target = -nums[i]
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result

solution = Solution()
nums1 = [0, 1, 1]
print("Test Case 1:", solution.threeSum(nums1))  # Output: []

nums2 = [-5, 0, 5, 10, -10, 0]
print("Test Case 2:", solution.threeSum(nums2))  # Output: [[-10, 0, 10], [-5, 0, 5]]
