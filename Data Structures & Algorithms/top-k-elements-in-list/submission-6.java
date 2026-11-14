class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int n: nums) {
            cnt.put(n, cnt.getOrDefault(n, 0) + 1);
        }

        Map<Integer, List<Integer>> cntToElList = new HashMap<>();
        for (Map.Entry<Integer, Integer> entry: cnt.entrySet()) {
            if (!cntToElList.containsKey(entry.getValue())) {
                cntToElList.put(entry.getValue(), new ArrayList<>());
            }
            cntToElList.get(entry.getValue()).add(entry.getKey());
        }

        int[] res = new int[k];
        int c = 0;
        for (int i = 10000; i >= 1; i--) {
            if (cntToElList.containsKey(i)) {
                for (int a: cntToElList.get(i)) {
                    res[c] = a;
                    c+=1;
                    if (c == k) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}
