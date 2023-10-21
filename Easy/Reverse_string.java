public class Reverse_string {
    public static void reverseString(char[] s) {
        int startPointer = 0;
        int endPointer = s.length;
        char c;

        while (startPointer < endPointer) {
            c = s[startPointer];
            s[startPointer] = s[endPointer];
            s[endPointer] = c;
            startPointer++;
            endPointer--;
        }
    }
}
