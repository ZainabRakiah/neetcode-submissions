class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        k = r = max(piles)
        while l<=r:
            hrs=0
            mid = l+(r-l)//2
            for i in piles:
                hrs+=i//mid
                if i%mid!=0:
                    hrs+=1
                
            if hrs <= h:
                r = mid-1
                k=mid
            else:
                l = mid+1
        return k

                
