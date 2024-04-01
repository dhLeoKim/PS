import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj1920 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1920.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            boolean flag = false;
            int target = Integer.parseInt(st.nextToken());
            int start = 0;
            int end = N-1;

            // 이진탐색 구현
            while (start <= end) {
                int mid_idx = (start+end)/2;
                int mid_val = A[mid_idx];
                if (mid_val > target) {
                    end = mid_idx-1;
                } else if (mid_val < target) {
                    start = mid_idx+1;
                } else {
                    flag = true;
                    break;
                }
            }

            if (flag) System.out.println(1);
            else System.out.println(0);
        }
    }
}