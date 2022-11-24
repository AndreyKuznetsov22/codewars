class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m, n = 0, len(arr)
        while m < n:
            mid = (m + n) // 2
            if arr[mid] - mid - 1 < k:
                m = mid + 1
            else:
                n = mid
        return n + k