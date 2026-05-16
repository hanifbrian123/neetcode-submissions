class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> prefMax(n);
        // Get Prefix Maximum
        prefMax[0] = height[0];
        int max = height[0];
        for (int i = 1; i < n; i++)
        {
            if (height[i]>max) {
                prefMax[i] = height[i];
                max = height[i];
            } else {
                prefMax[i] = max;
            }
        }

        vector<int> suffMax(n);
        // Get suffix Maximum
        suffMax[n-1] = height[n-1];
        int max2 = height[n-1];
        for (int i = n-2; i >= 0; i--)
        {
            if (height[i]>max2) {
                suffMax[i] = height[i];
                max2 = height[i];
            } else {
                suffMax[i] = max2;
            }
        }
        
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            res += min(prefMax[i], suffMax[i]) - height[i];
        }
        return res;
    }

    void printV(vector<int> &v) {
        for (int a: v)
        {
            cout<< a<< ' ';
        }
        cout<< endl;
    }
};