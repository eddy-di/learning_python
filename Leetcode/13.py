# from https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        subtracted_ints = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        usual_ints = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        subtracted_ints_dict = {}
        usual_ints_dict = {}
        for k, v in subtracted_ints.items():
            if k in s:
                subtracted_ints_dict[k] = subtracted_ints_dict.get(k, 0) + v
                s = s.replace(k, '')
        for i in s:
            if i in usual_ints:
                usual_ints_dict[i] = usual_ints_dict.get(i, 0) + usual_ints[i]
        
        subtracted_ints_res = sum([v for v in subtracted_ints_dict.values()])
        usual_ints_res = sum([v for v in usual_ints_dict.values()])

        return subtracted_ints_res + usual_ints_res

s1 = "III" # 3
s2 = "LVIII" # 58
s3 = "MCMXCIV" # 1994

print(Solution().romanToInt(s1))
print(Solution().romanToInt(s2))
print(Solution().romanToInt(s3))