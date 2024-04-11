import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println("Is \"" + t + "\" an anagram of \"" + s + "\"? " + isAnagram(s, t));
    }

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}

//Output: Is "nagaram" an anagram of "anagram"? true
