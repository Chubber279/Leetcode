import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        HashMap<Character, Integer> characters = new HashMap<>();
        Character c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (characters.keySet().contains(c)) {
                int value = characters.get(c);
                value++;
                characters.replace(c, value);
            } else {
                characters.put(c, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            c = t.charAt(i);
            if (characters.keySet().contains(c)) {
                int value = characters.get(c);
                value--;
                characters.replace(c, value);
            }
        }

        for (Character key : characters.keySet()) {
            if (characters.get(key) != 0)
                return false;
        }
        return true;
    }

    public boolean isAnagramArray(String s, String t) {
        int[] characters = new int[26];

        for (char c : s.toCharArray()) {
            characters[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            characters[c - 'a']--;
        }

        for (int i : characters) {
            if (i != 0)
                return false;
        }
        return true;
    }
}