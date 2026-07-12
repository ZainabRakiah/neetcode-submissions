class Solution {
    // Using long long for total hours to prevent integer overflow 
    // if h is small and piles are large.
    long long calculateHours(vector<int>& piles, int k){
        long long res = 0;
        for(int i = 0; i < piles.size(); i++){
            // Efficient way to do ceil(piles[i] / k) with integers
            res += (piles[i] + k - 1LL) / k;
        }
        return res;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = 0;
        
        // Find the maximum pile size for our upper bound
        for(int pile : piles) {
            r = max(r, pile);
        }
        
        int ans = r;
        
        while(l <= r){
            int mid = l + (r - l) / 2;
            long long time = calculateHours(piles, mid);
            
            if(time <= h){
                ans = mid;     // mid is a feasible speed, record it
                r = mid - 1;   // try to find a slower (smaller) speed
            } else {
                l = mid + 1;   // too slow, need a faster speed
            }
        }
        return ans;
    }
};