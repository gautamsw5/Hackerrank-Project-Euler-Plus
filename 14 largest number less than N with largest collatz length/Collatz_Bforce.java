import java.io.*;
import java.util.*;

public class Collatz_Bforce
{
    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        long start=System.currentTimeMillis();
        Scanner sc = new Scanner(System.in);
        int m=0,ans=0;
        int[] dct = new int[5000001];
        int[] dct2 = new int[5000001];
        dct[1]=0;
        dct2[1]=0;
        for(int i=2;i<5000001;i++)
        {
            int c=0;
            long x=i;
            while(x!=1)
            {   if(x%2==0)
                {
                    x=x/2;
                }
                else
                {
                    x=x*3+1;
                }
                c=c+1;
            }
            dct[i]=c;
            if(c>=m)
            {
                m=c;
                ans=i;
            }
            if(ans>dct2[i-1])
                dct2[i-1]=ans;
            else
                dct2[i]=dct2[i-1];
        }
        long end=System.currentTimeMillis();
        System.out.println(end-start);
        int t=sc.nextInt();
        for(int i=0;i<t;i++)
        {   int n=sc.nextInt();
            System.out.println(dct2[n-1]);
        }
    }
}