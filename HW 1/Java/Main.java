public class Main {
    public static void main(String[] args) {
        String s = "Ama!";
        System.out.println("Is \"" + s + "\" a palindrome? " + isPalindrome(s));
    }

    public static boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase(); // Remove non-alphanumeric characters and convert to lowercase
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}

//Output: Is "A man, a plan, a canal, Panama!" a palindrome? true