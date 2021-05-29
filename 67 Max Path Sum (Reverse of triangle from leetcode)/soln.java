import java.io.*;
import java.util.*;

public class Solution {
    private Map<Integer,Integer> map;
    private static int encode(int i , int j)
    {
        return i*10000+j;
    }
    private static int getminPath(List<List<Integer>> A, int i, int j, Map<Integer,Integer> map)
    {
        if(i+2==A.size())
        {
            if(j>0 && j<A.get(i).size()-1)
            {
                return A.get(i).get(j)+Math.max(A.get(i+1).get(j),A.get(i+1).get(j+1));
            }
            else if(j+1<A.size())
            {
                return A.get(i).get(j)+Math.max(A.get(i+1).get(j),A.get(i+1).get(j+1));
            }
            else
            {
                return A.get(i).get(j)+A.get(i+1).get(j);
            }
        }
        if(i+1==A.size())
        {
            return A.get(i).get(j);
        }
        int b=0,c=0;
        if(j+1<A.size() && i+1<A.size())
        {
            if(map.containsKey(encode(i+1,j+1)))
            {
                b=A.get(i).get(j)+map.get(encode(i+1,j+1));
            }
            else
            {
                b=A.get(i).get(j)+getminPath(A,i+1,j+1,map);
                map.put(encode(i+1,j+1),b-A.get(i).get(j));
            }
        }
        if(j<A.size() && i+1<A.size())
        {
            if(map.containsKey(encode(i+1,j)))
            {
                c=A.get(i).get(j)+map.get(encode(i+1,j));
            }
            else
            {
                c=A.get(i).get(j)+getminPath(A,i+1,j,map);
                map.put(encode(i+1,j),c-A.get(i).get(j));
            }
        }
        return Math.max(b,c);
    }
    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int m=Integer.MAX_VALUE;
        Map<Integer,Integer> map;
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        for(int xyz=0;xyz<t;xyz++)
        {
            int n=sc.nextInt();
            List<List<Integer>> list = new ArrayList<List<Integer>>();
            map = new HashMap<Integer,Integer>();
            for(int i=0;i<n;i++)
            {
                List<Integer> z = new ArrayList<Integer>();
                for(int j=0;j<i+1;j++)
                {
                    int x=sc.nextInt();
                    z.add(x);
                }
                list.add(z);
            }
            System.out.println(getminPath(list,0,0,map));
        }
    }
}