import java.util.HashMap;

public class LongestPalindrome {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }
        int maxLength = 0;
        boolean oddFrequencySeen = false;
        for (int frequency : frequencyMap.values()) {
            if (frequency % 2 == 0) {
                maxLength += frequency;
            } else {
                maxLength += frequency - 1;
                oddFrequencySeen = true;
            }
        }
        return oddFrequencySeen ? maxLength + 1 : maxLength;
    }

    public static void main(String[] args) {
        LongestPalindrome solution = new LongestPalindrome();
        String s1 = "abccccdd";
        System.out.println("Test Case 1: " + solution.longestPalindrome(s1)); //Output: 7

        String s2 = "speediskey";
        System.out.println("Test Case 2: " + solution.longestPalindrome(s2)); // Output: 5
    }
}
