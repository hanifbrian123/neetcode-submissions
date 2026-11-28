class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) return new int[][] {newInterval};
        List<int[]> intervalList = new ArrayList<>();
        for (int[] i: intervals) intervalList.add(i);
        intervalList.add(new int[] {Integer.MAX_VALUE, Integer.MAX_VALUE});

        int befEnd = -1;
        int resIdx = -1;
        for (int i=0; i<intervals.length; i++) {
            int[] interval = intervals[i];
            if (befEnd < newInterval[0] && newInterval[1] < interval[0]) resIdx = i;
            befEnd = interval[1];
        }
        intervalList.remove(intervalList.size()-1);
        
        if (resIdx != -1) {
            intervalList.add(resIdx, newInterval);
            int[][] res = new int[intervals.length + 1][2];
            for (int i=0; i<intervals.length+1; i++) {
                res[i][0] = intervalList.get(i)[0];
                res[i][1] = intervalList.get(i)[1];
            }
            return res;
        }

        // orverlap
        int start = -1; int end = -1;
        for (int i=0; i<intervals.length; i++) {
            int[] interval = intervals[i];
            if (newInterval[0] <= interval[0] || newInterval[0] <= interval[1]) {
                start = i;
                end = i;
                break;
            }
        }
        for (int i=start; i<intervals.length; i++) {
            if (newInterval[1] < intervals[i][0]) break;
            end = i;
        }
        // System.out.println(start + " " + end);
        int[] updatedInterval = new int[] {
            Math.min(intervals[start][0], newInterval[0]),
            Math.max(intervals[end][1], newInterval[1])
        };

        List<int[]> resList = new ArrayList<>();
        for (int i=0; i<intervals.length; i++)
            if (i < start || i > end) resList.add(intervals[i]);
        resList.add(start, updatedInterval);
        
        int[][] res = new int[resList.size()][2];
        for (int i=0; i<resList.size(); i++) {
            res[i][0] = resList.get(i)[0];
            res[i][1] = resList.get(i)[1];
        } 
        return res;
        
        



    }
}




//   |----| |--| |--|
// -1 .. [1,2],[3,5],[9,10]
// 0

// [6,7]

// - how to get the end point: if the start_i smaller or equal you overlap. if not smaller or equal, you break the while, and last the overlap one is the end point
// - how to get the start point: if the start_i greater you make it as a start point

// start > i_start: move
// start < i_end: stay start else
    