import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj1874 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1874.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bufferedReader.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(bufferedReader.readLine());
        }

        Stack<Integer> stack = new Stack<>();
        int num = 1;
        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < N; i++) {
            int arr_num = arr[i];
            if(arr_num >= num) {
                while (arr_num >= num) {
                    stack.push(num++);
                    stringBuffer.append("+\n");
                }
                stack.pop();
                stringBuffer.append("-\n");
            } else {
                int temp = stack.pop();
                if (temp > arr_num) {
                    System.out.println("NO");
                    return;
                } else {
                    stringBuffer.append("-\n");
                }
            }

        }
        System.out.println(stringBuffer);
//        System.out.println(stringBuffer.toString());
    }
}
