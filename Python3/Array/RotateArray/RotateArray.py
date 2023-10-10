from typing import List
nums = [1,2,3,4,5,6,7]
k = 3

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Calculate effective rotation steps

        # Create a copy of nums to avoid modifying it while iterating
        bufnums = nums[:]

        for i in range(n):
            nums[(i + k) % n] = bufnums[i]
            






solution_instance = Solution()
x = solution_instance.rotate()
print(x)