class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0]:
            prefix=strs[0]
        else:
            return ""
        for i in range(1,len(strs)):
            temp=""
            for j in range(min(len(prefix),len(strs[i]))):
                
                if (prefix[j]==strs[i][j]):
                    temp+=prefix[j]
                else:
                    break
            prefix=temp
            if not prefix:
                return ""
        return prefix

