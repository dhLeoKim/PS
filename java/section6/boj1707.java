import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class boj1707 {

    static ArrayList<Integer>[] arr;
    static boolean[] chk;
    static boolean[] visited;
    static boolean ret;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1707.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        for (int t = 0; t < tc; t++) {
            String[] str = br.readLine().split(" ");
            int V = Integer.parseInt(str[0]);
            int E = Integer.parseInt(str[1]);

            arr = new ArrayList[V+1];
            chk = new boolean[V+1];
            visited = new boolean[V+1];
            ret = true;

            // 인접 리스트 초기화
            for (int i = 1; i < V+1; i++) {
                arr[i] = new ArrayList<Integer>();
            }
            // 인접 리스트에 input 받기
            for (int i = 0; i < E; i++) {
                str = br.readLine().split(" ");
                int u = Integer.parseInt(str[0]);
                int v = Integer.parseInt(str[1]);
                arr[u].add(v);
                arr[v].add(u);
            }

            for (int i = 1; i < V+1; i++) {
                if (ret) DFS(i);
                else break;
            }

            if (ret) System.out.println("YES");
            else System.out.println("NO");
        }
    }

    public static void DFS(int now){
        visited[now] = true;
        for (int nxt : arr[now]) {
            if (!visited[nxt]) {
                chk[nxt] = !chk[now];
                DFS(nxt);
            } else if (chk[now] == chk[nxt]) {
                    ret = false;
                    return;
            }
        }
    }
}
