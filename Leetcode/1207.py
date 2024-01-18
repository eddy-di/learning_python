# from https://leetcode.com/problems/unique-number-of-occurrences/description/

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        key_val = {}
        for i in arr:
            if i not in key_val:
                key_val[i] = key_val.setdefault(i, 1)
            else:
                key_val[i] = key_val.get(i, 0) + 1
        values = [v for v in key_val.values()]
        sorted_values = sorted(values)
        res = []
        for i in range(len(sorted_values)):
            for j in range(i+1, len(sorted_values)):
                if sorted_values[i] != sorted_values[j]:
                    res.append(True)
                else:
                    res.append(False)
        return all(res)
    

c1 = [1,2,2,1,1,3]
c2 = [1,2]
c3 = [-3,0,1,-3,1,1,1,-3,10,0]

ex = Solution()

print(ex.uniqueOccurrences(c1))
print(ex.uniqueOccurrences(c2))
print(ex.uniqueOccurrences(c3))