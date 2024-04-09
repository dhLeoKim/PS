import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class boj1753 {

    static boolean[] visited;
    static int[] d;
    static ArrayList<Node>[] arr;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1753.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        visited = new boolean[V+1];
        d = new int[V+1];
        arr = new ArrayList[V+1];

        // 초기화
        for (int i = 1; i < V+1; i++) {
            arr[i] = new ArrayList<Node>();
            d[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            arr[u].add(new Node(v, w));
        }

        dijkstra(K);

        for (int i = 1; i < V+1; i++) {
            if (d[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(d[i]);
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>(((o1, o2) -> o1.w - o2.w));
        d[start] = 0;
        priorityQueue.offer(new Node(start, 0));

        while (!priorityQueue.isEmpty()) {
            Node now = priorityQueue.poll();

            if (d[now.v] < now.w) continue;

            for (Node nxt: arr[now.v]) {
                int nxtCost = now.w + nxt.w;
                if (nxtCost < d[nxt.v]) {
                    d[nxt.v] = nxtCost;
                    priorityQueue.offer(new Node(nxt.v, nxtCost));
                }
            }
        }
    }
}

class Node {
    int v;
    int w;

    public Node (int v, int w) {
        this.v = v;
        this.w = w;
    }
}
