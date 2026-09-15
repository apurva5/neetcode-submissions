class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in top:
                top[nums[i]] += 1
            else:
                top[nums[i]] = 1
        arr = []
        for num, cnt in top.items():
            arr.append([cnt, num])
        arr.sort()        
        while len(res) <k:
            res.append(arr.pop()[1])
        return res
        