class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        
        current_size = 1
        max_size = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                current_size += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                current_size = 1

            max_size = max(max_size, current_size)
    
        return max_size