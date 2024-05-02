import java.util.Arrays;

public class CoinChange {

    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0; // 0 coins are needed to make amount 0
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        CoinChange cc = new CoinChange();

        int[] coins1 = {1, 2, 5};
        int amount1 = 11;
        System.out.println("Test Case 1:");
        System.out.println("Input: " + Arrays.toString(coins1) + ", " + amount1);
        System.out.println("Output: " + cc.coinChange(coins1, amount1));  // Output should be 3

        int[] coins2 = {2};
        int amount2 = 3;
        System.out.println("\nTest Case 2:");
        System.out.println("Input: " + Arrays.toString(coins2) + ", " + amount2);
        System.out.println("Output: " + cc.coinChange(coins2, amount2));  // Output should be -1

        int[] coins3 = {1};
        int amount3 = 0;
        System.out.println("\nTest Case 3:");
        System.out.println("Input: " + Arrays.toString(coins3) + ", " + amount3);
        System.out.println("Output: " + cc.coinChange(coins3, amount3));  // Output should be 0
    }
}
