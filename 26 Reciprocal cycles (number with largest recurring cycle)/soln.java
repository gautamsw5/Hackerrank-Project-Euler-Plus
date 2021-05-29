import java.util.*;

class Reciprocal_Cycles {
    public static void main(String[] args) {
        int m = 0, d = 0;
        int[] ans = new int[10001];
        for (int i = 1; i < 10001; i++) {
            Map<Integer, Integer> rem = new HashMap<Integer, Integer>();
            int q = 1, c = 0;
            while (true) {
                // System.out.println(c+" "+q);
                if (q == 0) {
                    c = 0;
                    break;
                }
                if (rem.containsKey(q)) {
                    c = c - rem.get(q);
                    break;
                }
                rem.put(q, c++);
                if (i > q) {
                    q = q * 10;
                } else {
                    int x = q / i;
                    q = (q - i * x) * 10;
                }
            }
            if (c > m) {
                m = c;
                d = i;
            }
            // System.out.println(i+" "+c);
            ans[i] = d;
        }
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int xyz = 0; xyz < t; xyz++) {
            int n = sc.nextInt();
            System.out.println(ans[n - 1]);
        sc.close();
        }
    }
}
