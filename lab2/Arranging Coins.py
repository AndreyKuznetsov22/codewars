class Solution:
    def arrangeCoins(self, n: int) -> int:
        arr = 0
        c = 1
        while n >= c:
            n-=c
            arr+=1
            c+=1       
        return arr