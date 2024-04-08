import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj2252 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_2252.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 인접리스트 초기화
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            arr.add(new ArrayList<>());
        }

        // 위상 정렬 위한 진입차수 초기화
        int[] indegree = new int[N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            arr.get(A).add(B);
            indegree[B]++;
        }

        // 위상 정렬
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int now = queue.poll();
            System.out.print(now + " ");
            for (int nxt : arr.get(now)) {
                indegree[nxt]--;
                if (indegree[nxt] == 0) {
                    queue.offer(nxt);
                }
            }
        }
    }
}
