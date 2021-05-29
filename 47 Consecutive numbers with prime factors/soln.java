import java.util.*;
import java.io.*;
public class Solution
{
    public static boolean[] ans;
    public static boolean prime(int n)
    {
        if(n%2==0)
        {
            return false;
        }
        int i=3;
        while(i*i<=n)
        {
            if(n%i==0)
            {
                return false;
            }
            i+=2;
        }
        return true;
    }
    public static int Pfactors(int n)
    {       Set<Integer> ret = new HashSet<Integer>();
            int i=2;
            while(i*i<=n)
            {   if(n%i==0)
                {   if(!ans[i])
                        ret.add(i);
                    if(!ans[n/i])
                        ret.add(n/i);
                    if(ret.size()>4)
                        break;
                }
                i=i+1;
            }
            return ret.size();
    }
    public static void main(String[] args)
    {   Scanner sc = new Scanner(System.in);
        int N=sc.nextInt()+1,k=sc.nextInt();
        ans = new boolean[N+4];
        for(int p = 2; p*p <N+4; p++)
        {
            if(ans[p] == false)
            {
                for(int i = p*p; i < N+4; i += p)
                    ans[i] = true;
            }
        }
        if(k==2)
        {
            for(int n=14;n<N;n++)
            {
                if(ans[n] && ans[n+1] && Pfactors(n)==2 && Pfactors(n+1)==2)
                    System.out.println(n);
            }
        }
        if(k==3)
        {
            for(int n=644;n<N;n++)
            {
                if(ans[n] && ans[n+1] && ans[n+2] && Pfactors(n)==3 && Pfactors(n+1)==3 && Pfactors(n+2)==3)
                    System.out.println(n);
            }
        }
        else if(k==4)
        {   
            for(int n=134043;n<N;n++)
            {
                if(ans[n] && ans[n+1] && ans[n+2] && ans[n+3] && Pfactors(n)==4 && Pfactors(n+1)==4 && Pfactors(n+2)==4 && Pfactors(n+3)==4)
                    System.out.println(n);
            }
        }
    }
}
