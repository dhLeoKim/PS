import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj11286 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11286.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(((o1, o2) -> {
            // 조건1. 절대값 작은 데이터 우선 출력
            // 조건2. 절대값이 같다면 더 작은 값 (음수) 출력
            int abs1 = Math.abs(o1);
            int abs2 = Math.abs(o2);
            if (abs1 == abs2){
                return o1 - o2;             // 작은값이 우선
            }
            return abs1 - abs2;             // 작은값이 우선
        }));

        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (priorityQueue.isEmpty()) {  // 조건3. 비어있으면 0출력
                    System.out.println("0");
                } else {                        // 조건4. 0을 입력받으면 조건에 맡게 숫자 출력
                    System.out.println(priorityQueue.poll());
                }
            } else {                            // 0입력 아니면 우선순위 큐에 저장
                priorityQueue.add(x);
            }
        }
    }
}