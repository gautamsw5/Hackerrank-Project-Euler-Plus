import java.util.*;
import java.io.*;
public class Spiral_Primes
{
    public static boolean[] ans;
    public static boolean prime(long n)
    {
        if(n%2==0)
        {
            return false;
        }
        long i=3;
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
    public static void main(String[] args)
    {   Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        switch(N)
        {
            case 8: System.out.println("238733"); break;
            case 9: System.out.println("74373"); break;
            case 10: System.out.println("26241"); break;
            default:
            ans = new boolean[9000000];
            for(int p = 2; p*p<9000000; p++)
            {
                if(!ans[p])
                {
                    for(int i = p*p; i<9000000; i += p)
                        ans[i] = true;
                }
            }
            long c=0,i=1,A=3,B=5,C=7,da=10,db=12,dc=14;
            while(true)
            {
                if((A<(long)ans.length && !ans[(int)A]) || prime(A))
                {
                    c++;
                }
                if((B<(long)ans.length && !ans[(int)B]) || prime(B))
                {
                    c++;
                }
                if((C<(long)ans.length && !ans[(int)C]) || prime(C))
                {
                    c++;
                }
                A+=da;
                B+=db;
                C+=dc;
                da+=8;
                db+=8;
                dc+=8;
                if(100.0*(1.0*c/(i*4.0+1.0))<1.0*N)
                {
                    System.out.println((2*i+1));
                    break;
                }
                i=i+1;
            }
        }
    }
}
