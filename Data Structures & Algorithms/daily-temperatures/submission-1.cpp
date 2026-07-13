class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<pair<int,int>> st;
        for(int i=0; i<n;i++){
            while(!st.empty() && 
            st.top().first < temperatures[i]){
                int indx2 = st.top().second;
            result[indx2] = i - indx2;
                st.pop();
            }
            st.push({temperatures[i], i});
        }

        return result;
    }
};
