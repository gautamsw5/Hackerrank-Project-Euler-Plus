import java.io.*;
import java.util.*;

public class Solution
{
    public static void main(String[] args)
    {
        int i=3;
        Set<Integer> ans = new HashSet<Integer>();
        while(i<500001)
        {    boolean prime=true;
            if(i%2==0)
                prime=false;
            else
            {   int j=3;
                while(j*j<=i)
                {    if(i%j==0)
                     {   prime=false;
                        break;
                     }
                    j=j+2;
                }
            }
            if(prime)
                ans.add(i);
            i=i+2;
        }
        int[] dct=new int[250000];
        for(int p : ans)
        {   int k=1;
            while(p+2*k*k<500001)
            {   int n=p+2*k*k;
                if(!ans.contains(n))
                    dct[(n-9)/2]+=1;
                k=k+1;
            }
        }
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        for(int xyz=0;xyz<t;xyz++)
        {   int n=sc.nextInt();
            System.out.println(dct[(n-9)/2]);
        }
    }
}