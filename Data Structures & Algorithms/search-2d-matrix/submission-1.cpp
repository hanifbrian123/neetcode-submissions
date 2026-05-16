class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n = matrix.size(), m = matrix[0].size();
        int l = 0, r = m*n - 1;
        while (l<=r)
        {
            int la = matrix[l/m][l%m];
            int ra = matrix[r/m][r%m];

            int mid = (l+r)/2;
            int mida = matrix[mid/m][mid%m];
            
            if (mida == target) return true;
            else if (mida > target) r = mid - 1;
            else l = mid + 1;
        }
        return false;
        

    }
};