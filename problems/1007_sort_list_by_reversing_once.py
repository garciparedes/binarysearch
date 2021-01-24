class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return True

        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                break
            i += 1

        j = len(nums) - 1
        while i < j:
            if nums[j - 1] > nums[j]:
                break
            j -= 1

        if i == j:
            return True

        while i > 0:
            if nums[i] != nums[i - 1]:
                break
            i -= 1

        while j < len(nums) - 1:
            if nums[j] != nums[j + 1]:
                break
            j += 1

        if i > 0 and nums[i - 1] > nums[j]:
            return False
        if j < len(nums) - 1 and nums[i] > nums[j + 1]:
            return False

        print(i, j)
        for k in range(i, j):
            if nums[k] < nums[k + 1]:
                return False

        return True
