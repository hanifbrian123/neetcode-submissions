class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    public int carFleet(int target, int[] position, int[] speed) {
        for (int i = 0; i < position.length; i++) {
            map.put(position[i], speed[i]);
        }
        
        List<Integer> stack = new ArrayList<>();
        Arrays.sort(position);
        stack.add(position[position.length - 1]);
        int res = 1;

        for (int i = position.length - 2; i >= 0; i--) {
            while (
                !stack.isEmpty() && !canReach(position[i], stack.get(stack.size() - 1), target)
            ) {
                stack.remove(stack.size() - 1);
            }
            if (stack.isEmpty()) res++;
            stack.add(position[i]);
        }
        return res;

    }

    private boolean canReach(int pos1, int pos2, int target) {
        double timesPos2 = (double) (target - pos2) / map.get(pos2);
        return pos1 + timesPos2 * map.get(pos1) >= pos2 + timesPos2 * map.get(pos2);

    }
}
// target = 10
// 8 7 6 5 4 3



// target = 10
// 7 4 1 0

// stack = 0


// 0: 1
// 1: 2
// 4: 2
// 7: 1

// 4 1 0 7


// 0      1     4 7
// target = 10