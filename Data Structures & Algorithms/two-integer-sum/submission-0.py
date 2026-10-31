class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y = {}
        for i,n in enumerate(nums):
            f = target - n

            if f in y:
                return [y[f],i]
            y[n] = i
