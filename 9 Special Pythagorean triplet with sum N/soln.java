import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int m=-1;
            for(int a=1;a<n;a++)
            {
                double sum=1.0*n-1.0*a;
                double prod=(sum*sum-1.0*a*a)/2.0;
                if(sum*sum>4.0*prod && 1.0*a*prod>1.0*m)
                {
                    double D=Math.sqrt(sum*sum-4.0*prod);
                    if(Math.floor(D)==Math.ceil(D) && sum+D>0 && sum-D>0)
                    {
                        m=(int)(a*prod);
                    }
                }
            }
            System.out.println(m);
        }
    }
}