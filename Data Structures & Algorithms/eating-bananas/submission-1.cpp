class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int max = piles[0];
        for (int i = 1; i < piles.size(); i++)
        {
            if (piles[i] > max) max = piles[i];
        }
        int l = 1, r = max;
        while (l<r)
        {
            int mid = (l+r)/2;
            // cout<< mid<< endl;
            int hSpent = 0;
            for (int i = 0; i < piles.size(); i++)
            {
                hSpent += ((piles[i]-1) / mid) + 1;
            }
            if (hSpent<=h) r = mid;
            else l = mid+1;
        }
        // cout<< endl<< endl<< endl;
        return r;
    }
};