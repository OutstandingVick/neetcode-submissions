class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        shelves = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            shelves[freq].append(num)

        result = []
        for freq in range(len(shelves) - 1, 0, -1):
            for num in shelves[freq]:
                result.append(num)
                if len(result) == k:
                    return result