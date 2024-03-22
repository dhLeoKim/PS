import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class boj11720 {
    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("./input_11720.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sNum = sc.next();
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for(int i = 0; i < cNum.length; i++) {
//            sum += cNum[i] - '0';   // '0'을 빼거나, 아스키코드 값 48을 빼면 된다
            sum += Character.getNumericValue(cNum[i]); // 문자의 숫자값을 반환하는 메서드
        }

        System.out.println(sum);
    }
}
