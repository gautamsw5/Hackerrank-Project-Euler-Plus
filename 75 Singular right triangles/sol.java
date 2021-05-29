import java.util.*;
class Solution
{
    static int gcd(int a, int b)
    {
        if(b==0)
            return a;
        return gcd(b, a%b);
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = 5000001;
        int[] count = new int[N];
        int[] dp = new int[N];
        for(int m = 1; m < 1583; m++)
            for(int n=1+m%2; 2*m*m + 2*m*n < N && n<m; n+=2)
                if(gcd(n,m)==1)
                    for(int k=1; 2*m*m*k + 2*m*n*k < N ; k++)
                        count[2*m*m*k + 2*m*n*k] += 1;
        for(int i=1; i<N; i++)
        {
            dp[i] = dp[i-1];
            if(count[i]==1)
                dp[i]++;
        }
        int t;
        t = sc.nextInt();
        for(int o = 0; o < t; o++)
            System.out.println(dp[sc.nextInt()]);
        sc.close();
    }
}
