class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (int n: nums) {
            cnt.put(n, cnt.getOrDefault(n, 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>(
            Map.Entry.comparingByValue(Collections.reverseOrder())
        );
        maxHeap.addAll(cnt.entrySet());

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = maxHeap.poll().getKey();
        }
        return res;

    }
}
