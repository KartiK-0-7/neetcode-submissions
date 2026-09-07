class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for chr in s:
            if chr.isalnum():
                new+=chr.lower()
        if(len(new)==0 or len(new)==1):
            return True
        first=0
        last=len(new)-1
        for i in range((len(new)//2)):
            if(new[first]!=new[last]):
                return False
                break
            first+=1
            last-=1
        return True