class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        t2_max = float("-inf")
        for l in range(len(nums)):
            if nums[l] == 1:
                t1_max = 1
            else:
                t1_max = nums[l]
                cur_mult = nums[l]
                for r in range(l+1, len(nums)):
                    cur_mult *= nums[r]
                    if cur_mult > t1_max:
                        t1_max = cur_mult
            if t1_max > t2_max:
                t2_max = t1_max
        return t2_max
                    class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        t2_max = float("-inf")
        for l in range(len(nums)):
            if nums[l] == 1:
                t1_max = 1
            else:
                t1_max = nums[l]
                cur_mult = nums[l]
                for r in range(l+1, len(nums)):
                    cur_mult *= nums[r]
                    if cur_mult > t1_max:
                        t1_max = cur_mult
            if t1_max > t2_max:
                t2_max = t1_max
        return t2_max
                    