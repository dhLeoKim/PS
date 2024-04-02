import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1541 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_1541.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int ret = 0;
        String input = br.readLine();
        String[] str = input.split("-");

        for (int i = 0; i < str.length; i++) {
            int temp = sumStr(str[i]);
            if (i == 0) ret += temp;
            else ret -= temp;
        }

        System.out.println(ret);
    }

    public static int sumStr(String subStr){
        int tempSum = 0;
        String[] tempStr = subStr.split("\\+");     // 문자열 + 다룰 때 주의! "\\+" 로 쓰거나 "[+]" 도 가능
        for (int i = 0; i < tempStr.length; i++) {
            tempSum = tempSum + Integer.parseInt(tempStr[i]);
        }
        return tempSum;
    }
}
