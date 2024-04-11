public class Main {
    public static void main(String[] args) {
        int n = 5; 
        System.out.println("First bad version: " + firstBadVersion(n));
    }

    public static int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private static boolean isBadVersion(int version) {
        int firstBadVersion = 4; 
        return version >= firstBadVersion;
    }
}

//Output: First bad version: 4