class Solution
{
    public static void main(String[] args)
    {
        int N = 60001, mod = 1000000007;
        int[] dp = new int[N];
        dp[0] = 1;
        for(int i=0; i<N; i++)//coin in coins:
            for(int j=i; j<N; j++)//k in range(coin,N+1):
            dp[j] = (dp[j] + dp[j-i])%mod;//dp[k] += dp[k-coin];
        System.out.println(dp[N-1]);
    }
}