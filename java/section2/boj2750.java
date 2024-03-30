import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj2750 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_2750.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 버블 정렬 구현 (ex 오름차순)
        // 0부터 N까지 바로 옆의 값과 비교하여 큰값을 스왑하며 뒤로 밀기
        // 0부터 N-1까지 다시 반복
        for (int i = 0; i < N-1; i++) {
            for (int j = 0; j< N-1-i; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
        }
    }
}