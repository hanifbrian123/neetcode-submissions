class Solution {
    int[] count = new int[26];
    public int characterReplacement(String s, int k) {
        int res = 0, l = 0; 
        count[ (int) s.charAt(l) - (int) 'A' ] ++;

        for (int r = 1; r < s.length(); r++) {
            count[ (int) s.charAt(r) - (int) 'A' ] ++;
            
            while ((r - l + 1) - getMaxFreq() > k) {
                count[ (int) s.charAt(l) - (int) 'A' ] --;
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
    private int getMaxFreq() {
        int ret = count[0];
        for (int i = 1; i < 26; i++) {
            ret = Math.max(ret, count[i]);
        }
        return ret;
    }
}

// c a a a a b a b b b
// """
// k = 2
// a a a b a b b


// k = 2
// k x y y x k


// x y y x

// 10^6

// maxv
// maxc
// map {
// - c: 1
// - a: 4
// }

// - move right pointer
//     - add the frequent element +1
//     - most frequent still lack
//         - move 


// a c a a a b b b c b a b




// k k k





// """