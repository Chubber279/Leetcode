public class Move_zeroes {
    public static void moveZeroes(int[] nums) {
        int zeroIndex = -1;
        boolean isZero = false;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0 && isZero == false) {
                zeroIndex = i;
                isZero = true;
            }
            if (nums[i] != 0 && isZero == true) {
                nums[zeroIndex] = nums[i];
                nums[i] = 0;
                zeroIndex++;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = { 0, 1, 0, 3, 12 };
        moveZeroes(nums);
    }
}
