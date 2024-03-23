import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj2018 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_2018.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int start = 1;
        int end = 1;
        int sum = 1;
        int ret = 0;
        while(end != N+1) {     // 종료 인덱스 조건 주의!
            if (sum == N) {
                ret++;
                end++;
                sum += end;
            } else if (sum > N) {
                sum -= start;
                start++;
            } else {
                end++;
                sum += end;
            }
        }

        System.out.println(ret);
    }
}
