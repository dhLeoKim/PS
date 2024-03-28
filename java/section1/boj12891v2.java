import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj12891v2 {

    static int[] chk_arr;
    static int[] my_arr;
    static int chk_pw;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_12891.txt"));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        char[] arr = new char[S];              // 인풋 문자열

        int ret = 0;
        chk_arr = new int[4];                 // 만족해야하는 조건 배열
        my_arr = new int[4];                  // 현재 윈도우인 부분문자열 배열
        chk_pw = 0;                           // 만족하는 조건의 개수, 4면 ACGT 모두 만족

        arr = bf.readLine().toCharArray();
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {               // 만족해야하는 조건을 chk_arr에 넣기
            chk_arr[i] = Integer.parseInt(st.nextToken());
            if (chk_arr[i] == 0) {
                chk_pw++;                           // 조건이 0인경우, 이미 조건 만족하니 ++
            }
        }

        for (int i = 0; i < P; i++) {
            Add(arr[i]);                       // 확인해야하는 길이P의 부분문자열 만들기
        }

        if (chk_pw == 4) ret++;

        //위도우 슬라이딩 구현
        for (int end = P; end < S; end++){
            int start = end-P;
            Add(arr[end]);                    // 마지막 문자열만 추가
            Remove(arr[start]);               // 첫번째 문자열만 제거
            if (chk_pw == 4) ret++;
        }

        System.out.println(ret);
    }

    public static void Add(char c){
        switch (c) {
            case 'A':
                my_arr[0]++;
                if (my_arr[0] == chk_arr[0]) chk_pw++;
                break;
            case 'C':
                my_arr[1]++;
                if (my_arr[1] == chk_arr[1]) chk_pw++;
                break;
            case 'G':
                my_arr[2]++;
                if (my_arr[2] == chk_arr[2]) chk_pw++;
                break;
            case 'T':
                my_arr[3]++;
                if (my_arr[3] == chk_arr[3]) chk_pw++;
                break;
        }
    }

    public static void Remove(char c){
        switch (c){
            case 'A':
                if(my_arr[0] == chk_arr[0]) chk_pw--;
                my_arr[0]--;
                break;
            case 'C':
                if(my_arr[1] == chk_arr[1]) chk_pw--;
                my_arr[1]--;
                break;
            case 'G':
                if(my_arr[2] == chk_arr[2]) chk_pw--;
                my_arr[2]--;
                break;
            case 'T':
                if(my_arr[3] == chk_arr[3]) chk_pw--;
                my_arr[3]--;
                break;
        }
    }
}