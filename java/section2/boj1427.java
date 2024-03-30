import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj1427 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1427.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int[] arr = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            arr[i] = Integer.parseInt(str.substring(i, i+1));
        }

        // 선택 정렬 구현 (ex 내림차순)
        // 최대값의 위치 찾기
        // 최대값의 위치와 정렬되어 하는 다음위치 스왑
        for (int i = 0; i < str.length(); i++) {
            int maxIdx = i;
            for (int j = i+1; j < str.length(); j++) {              // 최대값 찾기
                if (arr[j] > arr[maxIdx]) {
                    maxIdx = j;
                }
            }

            if (arr[i] < arr[maxIdx]) {                             // 최대값과 정렬되야하는 순서 위치 스왑하기
                int temp = arr[i];
                arr[i] = arr[maxIdx];
                arr[maxIdx] = temp;
            }
        }

        for (int i = 0; i < str.length(); i++) {
            System.out.print(arr[i]);
        }
    }
}