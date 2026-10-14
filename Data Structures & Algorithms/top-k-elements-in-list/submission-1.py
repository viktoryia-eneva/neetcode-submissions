class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        sorted_items = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
