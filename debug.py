class Solution:
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    def quickSort(self, nums, left, right):
        if left < right:
            pivotIndex = self.partition(nums, left, right, left)
            self.quickSort(nums, left, pivotIndex - 1)
            self.quickSort(nums, pivotIndex + 1, right)
        # return nums
    def partition(self, nums, left, right, pivotIndex):
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        storeIndex = left
        for i in range(left, right):
            if nums[i] < pivotValue:
                nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
                storeIndex += 1
        nums[storeIndex], nums[left] = nums[left], nums[storeIndex]
        return storeIndex

a  = [5,2,3,1]
solution = Solution()
print(solution.sortArray(a))