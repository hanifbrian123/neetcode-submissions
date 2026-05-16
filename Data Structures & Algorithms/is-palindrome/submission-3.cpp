class Solution {
public:
    bool isPalindrome(string s) {
        int l=0, r=s.size()-1;
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        while (l < r)
        {
            while (!isalnum(s[l]) && l<r)
            {
                l++;
            }
            while (!isalnum(s[r]) && l<r)
            {
                r--;
            }
            cout<< s[l]<< ' '<<  s[r]<< endl;
            if (s[l]!=s[r]) {
                return false;
            }
            l++; r--;
        }
        return true;
    }
};
