class Solution {
    public boolean isAnagram(String s, String t) {
        for (int i = 0; i < s.length(); i++) {
            if (!t.contains((String.valueOf(s.charAt(i)))))
                return false;
        }
        return true;
    }
}