# class Solution:
#     def nextPermutation(self, nums) -> None:
#         is_last = True
#         for i in range(len(nums) - 1):
#             if nums[i] < nums[i + 1]: is_last = False
#         if is_last:
#             nums.reverse()
#             return

#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] >= nums[i + 1]: continue
#             # 3, 8, 4, 2
#             # i,i+1,i+2,i+3
#             for j in range(len(nums) - 1, i, -1):
#                 if nums[j] > nums[i]:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     break
#             p, q = i + 1, len(nums) - 1
#             while(p < q):
#                 nums[p], nums[q] = nums[q], nums[p]
#                 p += 1
#                 q -+ 1
#             # nums[i+1:].sort()
#             # wrong as slice generate another list, not in place operation
#             break

# a = [5,4,7,5,3,2]
# s = Solution()
# s.nextPermutation(a)

print(list(6))