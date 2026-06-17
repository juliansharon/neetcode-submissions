class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_char_count = {}

        for c in t:
            t_char_count[c] =t_char_count.get(c,0) +1
        required_unique = len(t_char_count)

        l=0
        formed = 0
        window_char_count = {}  
        ans = (float('inf'), None, None)  
        for r in range(len(s)):
            if s[r] in t_char_count:
                window_char_count[s[r]]=window_char_count.get(s[r],0) +1
                if  window_char_count[s[r]] == t_char_count[s[r]]:
                    formed+=1
            while l<=r and formed == required_unique:
                char_left = s[l]
                current_len = r - l + 1
                if current_len < ans[0]:
                    ans = (current_len, l, r)
                if char_left in window_char_count:    
                    window_char_count[char_left] -= 1  
                if char_left in   t_char_count and window_char_count[char_left]< t_char_count[char_left]:
                    formed-=1
                l+=1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]                


        