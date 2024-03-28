import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj2164 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_2164.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new LinkedList<>();      // 큐 선언
        for (int i = 1; i < N+1; i++) {
            queue.add(i);
        }

        while (queue.size() > 1) {
            queue.poll();                               // 큐의 맨 앞값 poll
            queue.add(queue.poll());                    // 빼낸 앞값을 다시 add
        }

        System.out.println(queue.poll());
    }
}