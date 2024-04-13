import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj11050 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11050.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] dp = new int[N+1][N+1];
        for (int i = 0; i < N+1; i++) {
            dp[i][i] = 1;
            dp[i][0] = 1;
            dp[i][1] = i;
        }

        for (int i = 2; i < N+1; i++) {
            for (int j = 1; j < i; j++) {
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1];   // 조합 점화식
            }
        }

        System.out.println(dp[N][K]);
    }
}
