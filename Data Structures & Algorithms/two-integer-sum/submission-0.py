class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req={}
        res=[]
        for i in range(len(nums)):
            k=target-nums[i]
            if(nums[i] in req):
                return [req[nums[i]],i]
            req[k]=i # matching counterparts with indices
        
        return []