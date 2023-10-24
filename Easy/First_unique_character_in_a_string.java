import java.util.LinkedHashMap;
import java.util.Map;

public class First_unique_character_in_a_string {
    public static int firstUniqChar(String s) {
        Map<Character, Integer> chars = new LinkedHashMap<>();
        for (char c : s.toCharArray()) {
            int temp = chars.getOrDefault(c, 0);
            temp++;
            chars.put(c, temp);
        }
        System.out.println(chars.toString());
        for (Map.Entry<Character, Integer> entry : chars.entrySet()) {
            if (entry.getValue() == 1) {
                return s.indexOf(entry.getKey());
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(firstUniqChar("leet"));
    }
}
