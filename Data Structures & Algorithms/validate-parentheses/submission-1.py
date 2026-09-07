from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st=deque()
        close={")":"(","}":"{","]":"["}
        for chr in s:
            if chr in close:
                if st and st[-1]==close[chr]:
                    st.pop()
                else:
                    return False
            else:
                st.append(chr)

        return not st