class Solution {
public:
    int findMin(vector<int> &nums) {
        if (nums.size() < 1){
            return nums[0];
        }
        int l = 0, r = nums.size()-1, mid = l + (r-l)/2;
        if(nums[l] < nums[r]){ 
            return nums[l];
            }
        int mini = nums[r];
        while(l < r){
            mid = l + (r-l)/2;
            if(nums[mid] < mini){
                mini = nums[mid];
                r = mid;
            }
        else if(nums[mid] > mini){
                l = l+1;
        }
        else{
            l++;
        }
        }
        return mini;
    }
};
