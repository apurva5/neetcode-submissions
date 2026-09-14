class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_twosum = {}
         
        for i in range(len(nums)):
            if target - nums[i] in hash_twosum:
                return [hash_twosum[target - nums[i]], i]
            hash_twosum[nums[i]] = i
        