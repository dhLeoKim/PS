import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj1940 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1940.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine());
        int M = Integer.parseInt(bufferedReader.readLine());
        int[] arr = new int[N];
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        Arrays.sort(arr);

        int ret = 0;
        int start = 0;
        int end = N-1;
        while (start < end) {
            if (arr[start]+arr[end] < M) start++;
            else if (arr[start]+arr[end] > M) end--;
            else {
                ret++;
                start++;
                end--;
            }
        }

        System.out.println(ret);
    }
}
