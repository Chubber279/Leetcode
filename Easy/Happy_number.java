public class Happy_number {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;

        do {
            if (slow == 1)
                return true;
            slow = getSquare(slow);
            fast = getSquare(getSquare(fast));

        } while (slow != fast);
        return false;
    }

    public int getSquare(int n) {
        int result = 0;
        while (n > 0) {
            result += (int) Math.pow((n % 10), 2);
            n /= 10;
        }
        return result;
    }
}
