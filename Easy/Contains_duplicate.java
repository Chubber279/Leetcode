import java.util.HashMap;

public class Contains_duplicate {

    public static boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> duplicates = new HashMap<>();
        for (int num : nums) {
            if (duplicates.keySet().contains(num)) {
                return true;
            } else {
                duplicates.put(num, 1);
            }
            System.out.println(duplicates);
            // System.out.println(num);
        }

        return false;
    }

    public static void main(String[] args) {
        int[] nums = { 3, 3 };
        System.out.println(containsDuplicate(nums));
    }
}
