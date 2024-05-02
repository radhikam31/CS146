def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins are needed to make amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    coins1 = [1, 2, 5]
    amount1 = 11
    print("Test Case 1:")
    print("Input:", coins1, amount1)
    print("Output:", coinChange(coins1, amount1))  # Output should be 3

    coins2 = [2]
    amount2 = 3
    print("\nTest Case 2:")
    print("Input:", coins2, amount2)
    print("Output:", coinChange(coins2, amount2))  # Output should be -1

    coins3 = [1]
    amount3 = 0
    print("\nTest Case 3:")
    print("Input:", coins3, amount3)
    print("Output:", coinChange(coins3, amount3))  # Output should be 0

if __name__ == "__main__":
    main()
