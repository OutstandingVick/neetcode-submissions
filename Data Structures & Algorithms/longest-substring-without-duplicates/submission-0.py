class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chartSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in chartSet:
                chartSet.remove(s[l])
                l += 1
            chartSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
        