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
                !stack.isEmpty()
                && numTimesReq(position[i], target) > numTimesReq(stack.get(stack.size() - 1), target)
            ) {
                stack.remove(stack.size() - 1);
            }
            if (stack.isEmpty()) res++;
            stack.add(position[i]);
        }
        return res;

    }

    private int numTimesReq(int pos, int target) {
        return Math.ceilDiv(target - pos, map.get(pos));
    }
}
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