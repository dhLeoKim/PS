import java.io.*;
import java.util.StringTokenizer;

public class boj1717 {

    static int[] p;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1717.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 대표 배열 초기화
        p = new int[N+1];
        for (int i = 0; i < N+1; i++) {
            p[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (c == 0) union(a, b);
            else if (c == 1) System.out.println(chkParent(a, b));
        }
    }

    public static int find(int now) {
        if (now == p[now]) return now;
        else return find(p[now]);
    }

    public static void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) p[pb] = pa;
    }

    public static String chkParent(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb) return "YES";
        else return "NO";
    }
}
