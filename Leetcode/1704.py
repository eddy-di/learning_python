# from https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        length = len(s)
        half = length / 2
        a = s[:half]
        b = s[half:]
        counter_a = 0
        counter_b = 0
        for i in a:
            if i in vowels:
                counter_a += 1
        for j in b:
            if j in vowels:
                counter_b += 1
        return counter_b == counter_a
