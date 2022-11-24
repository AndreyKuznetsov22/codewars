class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length = len(names)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if heights[i] < heights[j]:
                    names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]
        return names