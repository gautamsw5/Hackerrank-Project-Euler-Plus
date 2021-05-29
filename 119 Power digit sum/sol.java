import java.util.*;
import java.math.*;
class Solution
{
    static BigInteger b;
    static BigInteger sum_toB(BigInteger n)
    {
        BigInteger ans = new BigInteger("0");
        while(n.compareTo(BigInteger.ZERO)>0)
        {
            ans = ans.add(n.mod(b));
            n = n.divide(b);
        }
        return ans;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        b = new BigInteger(""+sc.nextInt());
        BigInteger MAX = (new BigInteger("10")).pow(100);
        List<BigInteger> ans = new ArrayList<>();
        BigInteger lim = new BigInteger("16000");
        for(BigInteger s = new BigInteger("2"); lim.compareTo(s) > 0; s = s.add(BigInteger.ONE))
        {
            BigInteger n = s;
            while(MAX.compareTo(n)>0)
            {
                if(s.equals(sum_toB(n)) && n.compareTo(b) >= 0)
                    ans.add(n);
                n = n.multiply(s);
            }
        }
        Collections.sort(ans, new Comparator<BigInteger>()
        {
            public int compare(BigInteger a, BigInteger b)
            {
                return a.compareTo(b);
            }
        });
        StringBuilder print = new StringBuilder("");
        for(BigInteger s:ans)
        {
            print.append(s+" ");
        }
        System.out.println(print);
        sc.close();
    }
}