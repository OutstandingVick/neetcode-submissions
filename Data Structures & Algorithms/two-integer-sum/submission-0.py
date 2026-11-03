class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            partner = target - nums[i]

            if partner in seen:
                return [seen[partner], i]

            seen[nums[i]] = i
 
        