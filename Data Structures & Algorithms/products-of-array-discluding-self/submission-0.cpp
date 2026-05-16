class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> forw(n);
        vector<int> backw(n);
        forw[0] = nums[0];
        backw[n-1] = nums[n-1];
        for (int i = 1; i < n; i++)
        {
            forw[i] = forw[i-1]*nums[i];
            backw[n-1-i] = backw[n-i]*nums[n-1-i];
        }
        
        vector<int> res(n);
        res[0] = backw[1];
        res[n-1] = forw[n-2];
        for (int i = 1; i <= n-2; i++)
        {
            res[i] = forw[i-1]*backw[i+1];
        }
        return res;
        
        
        
    }
};