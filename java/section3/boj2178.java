import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj2178 {

    static int[] di = {0, -1, 0, 1};
    static int[] dj = {-1, 0, 1, 0};
    static boolean[][] visited;
    static int[][] arr;
    static int N, M;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_2178.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < M; j++){
                arr[i][j] = Integer.parseInt(temp.substring(j, j+1));
            }
        }

        BFS(0, 0);

        System.out.println(arr[N-1][M-1]);
    }

    public static void BFS(int si, int sj) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {si, sj, 1});
        visited[si][sj] = true;

        while (!queue.isEmpty()) {
            int now[] = queue.poll();
            int i = now[0];
            int j = now[1];
            int cnt = now[2];

            for (int k = 0; k < 4; k++) {
                int ni = i + di[k];
                int nj = j + dj[k];
                if (ni >= 0 && ni < N && nj >= 0 && nj < M && arr[ni][nj] != 0 && !visited[ni][nj]) {
                    visited[ni][nj] = true;
                    arr[ni][nj] = cnt+1;
                    queue.offer(new int[] {ni, nj, cnt+1});
                }
            }
        }
    }
}
