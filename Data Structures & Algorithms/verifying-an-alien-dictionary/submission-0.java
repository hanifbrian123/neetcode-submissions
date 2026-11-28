class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> priority = new HashMap<>();
        for (int i = 25; i >= 0; i--)
            priority.put(order.charAt(25 - i), i);
        for (int i = 1; i < words.length; i++) {
            String a = words[i - 1];
            String b = words[i];
            if (!check(a, b, priority, words)) return false;
        }
        return true;
    }
    private boolean check(String a, String b, Map<Character, Integer> p, String[] words) {
        int i = 0;
        int minL = Math.min(a.length(), b.length());
        while (i < minL) {
            if (p.get(a.charAt(i)) > p.get(b.charAt(i))) return true;
            else if (p.get(a.charAt(i)) < p.get(b.charAt(i))) return false;
            i++;
        }
        return a.length() < b.length();
    }
}