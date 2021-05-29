import java.util.*;
import java.io.*;
class Sol
{
    public static void main(String[] args)
    {
        int N = 1000001;
        List<List<Integer>> fact = new ArrayList<>();
        for(int i=0; i<N; i++)
            fact.add(new ArrayList<>());
        for(int i=4; i<N; i+=2)
            fact.get(i).add(2);
        for(int i=3; i<N; i+=2)
        {
            if(fact.get(i).size()==0)
                for(int j=2*i; j<N; j+=i)
                    fact.get(j).add(i);
        }
        int[] dp = new int[N];
        for(int i=2; i<N; i++)
        {
            dp[i] = dp[i-1]+i-1;
            Set<Integer> s = new HashSet<>();
            for(int f :fact.get(i))
            {
                for(int k=f; k<i; k+=f)
                    s.add(k);
            }
            dp[i] -= s.size();
        }
        try
        {
            FileWriter myWriter = new FileWriter("filename.txt");
            myWriter.write(Arrays.toString(dp));
            myWriter.close();
        }
        catch(Exception e)
        {
            System.out.println("Error");
        }
    }
}