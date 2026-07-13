class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result;
        for(int i=0; i<n; i++){
            int cnt = 1;
            for(int j= i+1; j < n; j++){
                if(temperatures[i] < temperatures[j]){
                     result.push_back(cnt);
                     break;
                }
                if(j == n-1){result.push_back(0);}
                 cnt++;
            }
            if(i == n-1){result.push_back(0);}
        }
        return result;
    }
};
