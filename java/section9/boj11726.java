import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj11726 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11726.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long[] dp = new long[N+5];
        dp[1] = 1;
        dp[2] = 2;

        if (N >= 3) {
            for (int i = 3; i < N+1; i++) {
                // N이 1000에 가까워지면 long의 범위도 벗어나기 때문에
                // 매 dp 루프마다 나머지 연산 해아함!!
                dp[i] = (dp[i-1] + dp[i-2])%10007;
            }
        }

        System.out.println(dp[N]);
//        System.out.println(dp[N]&10007);  // 이렇게 나머지 연산 처리하면 overflow 발생
    }
}
