## 백준 파일 제출 폼

### input 입력받기
* FileInputStream
* Scanner
* nextInt()
* next()

```java
import java.io.FileInputStream;                                     // 입력 - 제출시 지우기
import java.io.IOException;                                         // 입력
import java.util.Scanner;                                           // 입력

// 제출시 클래스명 Main으로 수정
public class boj11720 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input_11720.txt"));     // txt 파일 읽어오기 - 제출시 지우기
        Scanner sc = new Scanner(System.in);                        // Scanner로 입력 받기
        int N = sc.nextInt();                                       // nextInt()로 정수 입력받기
        String sNum = sc.next();                                    // next()로 문자열 입력 받기
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for(int i = 0; i < cNum.length; i++) {
//            sum += cNum[i] - '0';
            sum += Character.getNumericValue(cNum[i]);
        }

        System.out.println(sum);
    }
}

```

### 데이터 타입(문자열, 정수)
* toCharArray()

#### char -> int
1. 아스키코드 이용
```java
int num = '1' - '0'; //  49(문자열 '1' 아스키값) - 48(문자열 '0' 아스키값) 
```
2. getNumericValue
```java
char cNum = '1';
int num = Character.getNumericValue(cNum);
```

### string -> int
```java
String str = "25";
int num = Integer.parseInt(str);
```

### 자동형변환
```java
// sum, max, N 모두 int 이지만
// 100.0을 곱해 double로 자동 형변환
System.out.println(sum*100.0/max/N);
```

### input 입력받기 2
* FileInputStream
* BufferedReader
    * 예외 처리 필수
    * try catch 문 또는 IOException 사용
    * String으로 입력 받기에 필요에 따라 형변환
* StringTokenizer
    * StringTokenizer("문자열", "구분자", true/false)
    * 구분자로 분할하여 토큰화
    * 구분자 옵션 안쓰면 디폴트는 띄어쓰기로 분할
    * true/false로 구분자도 token취급 가능, 디폴트는 false
    * .nextToken()
    * 으로 하나의 토큰 사용
```java
// 입력
// 5 3

        System.setIn(new FileInputStream("./input_11659.txt"));
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());       // 한 줄을 문자열로 입력받기 : 5 3
        int N = Integer.parseInt(stringTokenizer.nextToken());                                  // 첫번째 : 5
        int M = Integer.parseInt(stringTokenizer.nextToken());                                  // 두번째 : 3
```
#### StringTokenizer vs Split
* StringTokenizer는 클래스
* StringTokenizer는 문자/문자열로 구분
* StringTokenizer결과는 문자열
* StringTokenizer는 빈 문자열을 토큰으로 인식x
* 
* Split은 String의 메서드
* Split은 정규표현식
* Split결과는 문자열 배열
* Split은 빈 문자열을 토큰으로 인식

#### BufferedReader vs Scanner
* 백준에서 input 입력시의 속도차이 발생
    * BufferedReader가 더 빠름
* BufferedReader
    * 입력받은 값을 8192char (16384 byte) 크기의 버퍼에 담아두었다가 한번에 전송
* Scanner
    * 입력즉시 전송, 정수, 소수, 문자 구분해서 입력


## 자료구조
### Stack
```java
Stack<Integer> stack = new Stack<>();
```
* push(): 스택의 맨 뒤에 요소를 추가합니다.
* pop(): 스택의 맨 뒤에 있는 요소를 제거하고 반환합니다.
* peek(): 스택의 맨 뒤에 있는 요소를 제거하지 않고 반환합니다.
* empty(): 스택이 비어 있는지 여부를 확인합니다. 비어 있으면 true를 반환하고, 그렇지 않으면 false를 반환합니다.
* search(Object o): 주어진 요소가 스택의 어디에 있는지 검색하여 그 위치를 반환합니다. 맨 뒤 요소의 위치는 1부터 시작합니다. (맨 뒤에서 부터 1세기)

### Queue
```java
Queue<Integer> queue = new LinkedList<>();
```
* add(): 큐에 요소를 추가합니다. 요소를 추가할 수 없는 경우 예외를 발생시킵니다.
* offer(): 큐에 요소를 추가합니다. 요소를 추가할 수 없는 경우 false를 반환합니다.
* remove(): 큐에서 요소를 제거하고 반환합니다. 큐가 비어있는 경우 예외를 발생시킵니다.
* poll(): 큐에서 요소를 제거하고 반환합니다. 큐가 비어있는 경우 null을 반환합니다.
* element(): 큐의 맨 앞에 있는 요소를 반환합니다. 큐를 변경하지 않고 요소를 가져옵니다. 큐가 비어있는 경우 예외를 발생시킵니다.
* peek(): 큐의 맨 앞에 있는 요소를 반환합니다. 큐를 변경하지 않고 요소를 가져옵니다. 큐가 비어있는 경우 null을 반환합니다.


### PrioirityQueue
```java
PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
```
* add(E e), offer(E e): 우선순위 큐에 요소를 추가합니다. (예외 발생 / false 반환)
* remove(), poll(): 우선순위가 가장 높은 요소를 제거하고 반환합니다. (예외 발생 / false 반환)
* peek(): 우선순위가 가장 높은 요소를 반환합니다. 제거하지는 않습니다. (null 반환)
* size(), isEmpty(): 우선순위 큐의 크기와 비어 있는지 여부를 반환합니다.
* clear(): 우선순위 큐의 모든 요소를 제거합니다.
* toArray(): 우선순위 큐의 요소들을 배열로 반환합니다.

### Comparator
* return값이 양수면 객체1이 객체2 뒤에 위치
* return값이 음수면 객체1이 객체2 앞에 위치
```java
return o1 - o2;
```
* 작은값이 우선되도록 함 -> 오름차순 정렬

```java
return o2 - o1;
```
* 큰값이 우선되도록 함 -> 내림차순 정렬


```java
// 여기서 o2가 prioirityqueue에 먼저 입력된 값, o1이 나중에 입력된 값이다!!
// 즉 -2, 2를 순서대로 add하면, o2 = -2, o1 = 2가 된다.

PriorityQueue<Integer> priorityQueue = new PriorityQueue<>((o1, o2) -> {
    int abs1 = Math.abs(o1);
    int abs2 = Math.abs(o2);

    // 오름차순 정렬 : 작은값이 제일 위로
    // 객체1이 객체2보다 크면, return 값이 양수 -> 객체1(큰값)이 객체2(작은값) 뒤에 위치 -> 오름차순으로 정렬
    // 객체1이 객체2보다 작으면, return 값이 음수 -> 객체1(작은값)이 객체2(큰값) 앞에 위치 -> 오름차순으로 정렬
    
    return abs1 - abs2;

    // 내림차순 정렬 : 큰값이 제일 위로
    // 객체2가 객체1보다 크면, return값이 양수 -> 객체1(작은값)이 객체2(큰값) 뒤에 위치 -> 내림차순으로 정렬 
    // 객체2가 객체1보다 작으면, return값이 음수 -> 객체1(큰값)이 객체2(작은값) 앞에 위치 -> 내림차순으로 정렬
    return abs2 - abs1; 
});
```