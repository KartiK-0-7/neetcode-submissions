class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        s=0
        l=[]
        while(i<j):
            s=numbers[i]+numbers[j]
            if(s<target):
                i+=1
            elif(s>target):
                j-=1
            else:
                i+=1
                j+=1
                l.append(i)
                l.append(j)
                return l