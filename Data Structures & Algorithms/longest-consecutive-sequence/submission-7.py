class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_size = 0

        for num in numbers:
            if num - 1 not in numbers:
                current_size = 1
                current_num = num

                while current_num + 1 in numbers:
                    current_num +=1
                    current_size += 1

                max_size = max(current_size, max_size)

        return max_size