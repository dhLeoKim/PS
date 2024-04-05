import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1929 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1929.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N+1];
        for (int i = 2; i <= N; i++) {
            arr[i] = i;
        }

        // 에라토스테네스의 체
        for (int i = 2; i <= Math.sqrt(N); i++) {
            if (arr[i] == 0) continue;  // 소수가 아닌 경우 continue
            for (int j = i+i; j <= N; j = j+i) {
                arr[j] = 0;             // 배수들은 소수가 아니므로 0 처리
            }
        }

        for (int i = M; i <= N; i++) {
            if (arr[i] != 0) System.out.println(arr[i]);
        }
    }
}
