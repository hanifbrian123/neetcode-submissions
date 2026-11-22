class Solution {
    public int rob(int[] nums) {
        int rob1 = 0, rob2 = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            int temp = rob1;
            rob1 = Math.max(rob2 + nums[i], temp);
            rob2 = temp;
        }
        int mx1 = Math.max(rob1, rob2);


        rob1 = 0; rob2 = 0;
        for (int i = 1; i < nums.length; i++) {
            int temp = rob1;
            rob1 = Math.max(rob2 + nums[i], temp);
            rob2 = temp;
        }
        int mx2 = Math.max(rob1, rob2);
        return Math.max(mx1, mx2);

    }
}



// 2   9   8   3   6
//     |       |


// 2   9   8   3   6
//     |       |

// int
// 2   9   8   3   6



// 2   9   8   6   6