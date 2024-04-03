import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj11724 {

    static boolean visited[];
    static ArrayList<Integer>[] lst;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11724.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visited = new boolean[N+1];

        // 인접리스트 구현
        lst = new ArrayList[N+1];
        for (int i = 1; i < N+1; i++) {
            lst[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            lst[u].add(v);
            lst[v].add(u);
        }

        int ret = 0;
        for (int i = 1; i < N+1; i++) {
            if(!visited[i]) {
                ret++;
                DFS(i);
            }
        }

        System.out.println(ret);
    }

    public static void DFS(int now){
        if (visited[now]) return;
        visited[now] = true;
        for (int nxt : lst[now]) {
            if (!visited[nxt]) {
                DFS(nxt);
            }
        }
    }
}