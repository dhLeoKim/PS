import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1717v2 {

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
            p[i] = -1;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (c == 1) System.out.println(chkParent(a, b));
            else if (find(a) != find(b)) union(a, b);           // 같은 정점을 union 시키는 경우도 고려하기!
        }
    }

    public static int find(int x) {
        if (p[x] < 0) return x;
        return find(p[x]);
    }

    public static void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (p[pa] == p[pb]) p[pa] -= 1;
        if (p[pa] < p[pb]) p[pb] = pa;
        else p[pa] = pb;
    }

    public static String chkParent(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb) return "YES";
        else return "NO";
    }
}
