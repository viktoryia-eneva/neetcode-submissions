class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        if len(s) != len(t):
            return False

        for num in s:
            first[num] = first.get(num, 0) + 1
        
        for num in t:
            second[num] = second.get(num, 0) + 1

        if first == second:
            return True
        else:
            return False