class Solution {
    public String longestPalindrome(String s) {
        int lMax = 0, rMax = 0, maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            int l = i-1, r = i+1, len = 1;

            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                len += 2; l--; r++;
            }
            if (len > maxLength) {
                maxLength = len;
                lMax = l+1;
                rMax = r-1;
            }
        }
        
        for (int i = 0; i < s.length(); i++) {
            int l = i, r = i+1, len = 0;

            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                len += 2; l--; r++;
            }
            if (len > maxLength) {
                maxLength = len;
                lMax = l+1;
                rMax = r-1;
            }

        }

        return s.substring(lMax, rMax+1);
    }
}


// O(n^2) => 10^6 < 10^8



// a b a b d