class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        x=len(nums)//2
        while(low<=high):
            if(nums[x]==target):
                return x
            elif(nums[x]<target):
                low=x+1
                x=low+(high-low)//2
            else:
                high=x-1
                x=low+(high-low)//2
        return -1