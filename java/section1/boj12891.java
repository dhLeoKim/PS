import java.util.*;
import java.io.*;

public class boj12891 {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./input_12891.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 전체 문자열의 길이
        int stringLen = Integer.parseInt(st.nextToken());
        // 부분 문자열의 길이 = 슬라이딩 윈도우의 길이
        int passwordLen = Integer.parseInt(st.nextToken());

        // 전체 문자열 리스트
        char[] list = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        // 비밀번호가 되기 위해 필요한 각 A, C, G, T의 개수
        int[] countList = new int[4];
        countList[0] = Integer.parseInt(st.nextToken()); // 필요한 A의 개수
        countList[1] = Integer.parseInt(st.nextToken()); // 필요한 C의 개수
        countList[2] = Integer.parseInt(st.nextToken()); // 필요한 G의 개수
        countList[3] = Integer.parseInt(st.nextToken()); // 필요한 T의 개수

        // 찾은 DNA 문자열의 개수
        int answer = 0;

        // 맨 처음 부분문자열 탐색
        for (int i = 0; i < passwordLen; i++) {
            int index = alphabetToIndex(list[i]);

            // 해당 문자열이 A,C,G,T중에 하나라면
            // 필요한 문자 개수에서 -1
            if(index >= 0) {
                countList[index] -= 1;
            }
        }

        // 해당 문자열이 DNA문자열인지 확인
        if (check(countList))
            answer += 1;

        for (int i = 1; i <= (stringLen - passwordLen); i++) {
            // 슬라이딩 윈도우가 이동하면서

            // 슬라이딩 윈도우가 옆으로 이동하면 지나간 문자에 대한 처리
            int index = alphabetToIndex(list[i-1]);
            if (index >= 0) {
                countList[index] += 1;
            }

            // 슬라이딩 윈도우가 옆으로 이동하면서 추가된 문자 처리
            index = alphabetToIndex(list[i + passwordLen -1]);
            if(index >= 0) {
                countList[index] -= 1;
            }

            // 해당 문자열이 DNA문자열인지 확인
            if (check(countList))
                answer += 1;
        }

        System.out.println(answer);
    }

    // 문자 개수를 통해서 조건을 만족하는지 판단하는 함수
    public static boolean check(int[] countList) {
        for (int j = 0; j < 4; j++) {
            // 필요한 문자가 1개 이상 있는 경우 조건을 만족하는 것이 아니므로 false 반환
            if (countList[j] > 0) {
                return false;
            }
        }
        // 필요한 최소 문자 개수 기준을 만족하므로 true를 반환
        return true;
    }

    // 문자가 A, C, G, T인지 체크하고
    // countList에서 해당 문자 개수를 위한 index를 반환
    public static int alphabetToIndex(char c) {
        // 문자가 A, C, G, T가 아니라면 -1을 반환
        int index = -1;

        switch (c) {
            case 'A': // countList에서 필요한 A의 개수는 countList[0]에서 관리
                index = 0;
                break;
            case 'C': // countList에서 필요한 C의 개수는 countList[1]에서 관리
                index = 1;
                break;
            case 'G': // countList에서 필요한 G의 개수는 countList[2]에서 관리
                index = 2;
                break;
            case 'T': // countList에서 필요한 T의 개수는 countList[3]에서 관리
                index = 3;
                break;
        }

        return index;
    }
}