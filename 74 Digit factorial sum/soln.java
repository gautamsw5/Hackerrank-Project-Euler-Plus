import java.util.*;
import java.io.*;
public class Digit_Fact_Cycles
{
    public static Integer[] dp;
    public static int[] fact;
    public static int getCt(int n)
    {
        int x=n,c=1;
        Set<Integer> set = new HashSet<Integer>();
        int s=0;
        while(n>0)
        {
            s=s+fact[n%10];
            n=n/10;
        }
        n=s;
        set.add(n);
        if(n==x)
        {
            return 1;
        }
        while(n!=x)
        {
            s=0;
            while(n>0)
            {
                s=s+fact[n%10];
                n=n/10;
            }
            n=s;
            c=c+1;
            if(set.contains(n) && n!=x)
            {
                break;
            }
            set.add(n);
            /*if(n<dp.length && dp[n]!=null && dp[n]==1)
            {
                dp[x]=1;
                return 1;
            }
            else if(n<dp.length && dp[n]!=null)
            {
                dp[x]=c+dp[n];
                return dp[x];
            }
        dp[x]=c;*/
        }
        return c;
    }
    public static void main(String[] args)
    {
        dp = new Integer[1000001];
        dp[0]=2;
        fact=new int[]{1,1,2,6,24,120,720,5040,40320,362880};
        for(int i=1;i<1000000;i++)
        {
            dp[i]=getCt(i);
        }
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        for(int xyz=0;xyz<t;xyz++)
        {
            int n=sc.nextInt(),l=sc.nextInt();
            int f=0;
            for(int i=0;i<n+1;i++)
            {
                if(dp[i]==l)
                {
                    System.out.print(i+" ");
                    f=1;
                }
            }
            if(f==1)
            {
                System.out.println();
            }
            else
            {
                System.out.println(-1);
            }
        }
    }
}
