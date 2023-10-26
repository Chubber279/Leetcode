package Medium;

import java.util.HashMap;

public class Longest_substring_without_repeating_characters {
    public static int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> chars = new HashMap<>();
        int startPointer = 0;
        int maxVal = 0;

        for (int endPointer = 0; endPointer < s.length(); endPointer++) {
            if (chars.containsKey(s.charAt(endPointer))) {
                startPointer = Math.max(chars.get(s.charAt(endPointer)) + 1, startPointer);
            }
            chars.put(s.charAt(endPointer), endPointer);
            maxVal = Math.max(maxVal, endPointer - startPointer + 1);
        }

        return maxVal;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }
}
