import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj11047 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11047.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(br.readLine());
        }

        // 그리디
        int cnt = 0;
        for (int i = N-1; i >= 0; i--) {
            if (A[i] <= K) {
                cnt += (K/A[i]);
                K = K%A[i];
            }
        }

        System.out.println(cnt);
    }
}