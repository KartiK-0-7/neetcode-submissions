class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=nums[0]
        c=1

        for i in range(1,len(nums)):
            if c==0:
                n=nums[i]
                c=1
            elif nums[i]==n:
                c+=1
            else:
                c-=1
        return n
        