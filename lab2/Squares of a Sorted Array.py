class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for item in A:
            B.append(item * item)
        return sorted(B)