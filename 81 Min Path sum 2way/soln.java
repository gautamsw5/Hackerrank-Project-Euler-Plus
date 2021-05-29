import java.io.*;
import java.util.*;

public class Solution
{
    private static long[][] dp;
    private static long[][] grid;
    private static long getu(int n, int m)
    {
        if(n==grid.length-1 && m==grid[0].length-1)
        {
            return grid[n][m];
        }
        long c=0,c2=0;
        if(n<grid.length-1 && m<grid[0].length-1)
        {
            if(dp[n+1][m]!=0)
            {
                c=grid[n][m]+dp[n+1][m];
            }
            else
            {
                dp[n+1][m]=getu(n+1,m);
                c=grid[n][m]+dp[n+1][m];
            }
            if(dp[n][m+1]!=0)
            {
                c2=grid[n][m]+dp[n][m+1];
            }
            else
            {
                dp[n][m+1]=getu(n,m+1);
                c2=grid[n][m]+dp[n][m+1];
            }
            return Math.min(c,c2);
        }
        if(n<grid.length-1)
        {
            if(dp[n+1][m]!=0)
            {
                c=grid[n][m]+dp[n+1][m];
            }
            else
            {
                dp[n+1][m]=getu(n+1,m);
                c=grid[n][m]+dp[n+1][m];
            }
            return c;
        }
        if(m<grid[0].length-1)
        {
            if(dp[n][m+1]!=0)
            {
                c2=grid[n][m]+dp[n][m+1];
            }
            else
            {
                dp[n][m+1]=getu(n,m+1);
                c2=grid[n][m]+dp[n][m+1];
            }
        }
        return c2;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        grid = new long[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                grid[i][j]=sc.nextInt();
            }
        }
        dp = new long[n][n];
        System.out.println(getu(0,0));
    }
}