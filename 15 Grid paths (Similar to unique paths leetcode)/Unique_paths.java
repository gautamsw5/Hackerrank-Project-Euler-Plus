import java.io.*;
import java.util.*;

public class Solution
{
    private static int[][] map;
    private static int getu(int m, int n)
    {
        if(m==1 && n==1)
        {
            return 1;
        }
        int c=0;
        if(n>1)
        {
            int t=0;
            if(map[m-1][n-2]!=0)
            {
                t=map[m-1][n-2];
            }
            else
            {
                t=getu(m,n-1);
                map[m-1][n-2]=t;
            }
            c=(c%1000000007+t%1000000007)%1000000007;
        }
        if(m>1)
        {
            int t=0;
            if(map[m-2][n-1]!=0)
            {
                t=map[m-2][n-1];
            }
            else
            {
                t=getu(m-1,n);
                map[m-2][n-1]=t;
            }
            c=(c%1000000007+t%1000000007)%1000000007;
        }
        return c;
    }
    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        map = new int[500][500];
        Scanner sc = new Scanner(System.in);
        getu(500,500);
        int t=sc.nextInt();
        for(int i=0;i<t;i++)
        {
            int n=sc.nextInt();
            int m=sc.nextInt();
            System.out.println(map[m][n]);
        }
    }
}