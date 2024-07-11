### 1. 조건에 맞는 도서 리스트 출력하기
* BOOK 테이블에서 2021년에 출판된 '인문' 카테고리에 속하는 도서 리스트를 찾아서 도서 ID(BOOK_ID), 출판일 (PUBLISHED_DATE)을 출력하는 SQL문을 작성해주세요.
결과는 출판일을 기준으로 오름차순 정렬해주세요.

```SQL
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE FROM BOOK
WHERE YEAR(PUBLISHED_DATE)=2021 AND CATEGORY='인문'
ORDER BY PUBLISHED_DATE ASC;
```

* 날짜형식 관련
  * DATE_FORMAT( , )
  * YEAR()
  * MONTH()
  * DAY()
  
### 2. 조건에 부합하는 중고거래 댓글 조회하기
* USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

```SQL
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS A
INNER JOIN USED_GOODS_REPLY AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE DATE_FORMAT(A.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC;
```

* 조인
```SQL
SELECT <열 목록>
FROM <테이블1>
INNER JOIN <테이블2>
<LEFT | RIGHT | FULL> OUTER JOIN <테이블2>
ON <조인 조건>
--교집합 빼고 출력 시--
WHERE A.KEY IS NULL 
WHERE B.KEY IS NULL
```

### 3. 3월에 태어난 여성 회원 목록 출력하기
* MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.

```SQL
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') FROM MEMBER_PROFILE
WHERE GENDER='W' AND MONTH(DATE_OF_BIRTH)='3' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;
```

* NULL 확인

### 4. 흉부외과 또는 일반외과 의사 목록 출력하기
* DOCTOR 테이블에서 진료과가 흉부외과(CS)이거나 일반외과(GS)인 의사의 이름, 의사ID, 진료과, 고용일자를 조회하는 SQL문을 작성해주세요. 이때 결과는 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 이름을 기준으로 오름차순 정렬해주세요.

```SQL
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC;
```

### 5. 과일로 만든 아이스크림 고르기
* 상반기 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서대로 조회하는 SQL 문을 작성해주세요.

```SQL
SELECT A.FLAVOR FROM FIRST_HALF AS A
LEFT JOIN ICECREAM_INFO AS B ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER > 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY A.TOTAL_ORDER DESC;
```

* LEFT : 왼쪽 테이블 모두 출력
* RIGHT : 오른쪽 테이블 모두 출력

### 6. 평균 일일 대여 요금 구하기
* CAR_RENTAL_COMPANY_CAR 테이블에서 자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력하는 SQL문을 작성해주세요. 이때 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림하고, 컬럼명은 AVERAGE_FEE 로 지정해주세요.

```SQL
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
```

* 평균 AVG
* 반올림 ROUND( , 자릿수)
  * N : 소숫점 아래 N번째 자리까지 표기
  * -N : 10^N 자리까지 표기
  * 0 : 1의 자리까지 표기

### 7. 재구매가 일어난 상품과 회원 리스트 구하기
* ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 결과는 회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.

```SQL
SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;
```

* 그룹별 연산 GROUP BY
* 그룹 중 조건 HAVING

### 8. 인기있는 아이스크림
* 상반기에 판매된 아이스크림의 맛을 총주문량을 기준으로 내림차순 정렬하고 총주문량이 같다면 출하 번호를 기준으로 오름차순 정렬하여 조회하는 SQL 문을 작성해주세요.

```SQL
SELECT FLAVOR FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;
```

### 9. 업그레이드 된 아이템 구하기
* 아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력하는 SQL 문을 작성해 주세요. 이때 결과는 아이템 ID를 기준으로 내림차순 정렬주세요.

```SQL
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY FROM ITEM_INFO AS A
INNER JOIN ITEM_TREE AS B
ON A.ITEM_ID = B.ITEM_ID
WHERE B.PARENT_ITEM_ID IN (
        SELECT ITEM_ID FROM ITEM_INFO
        WHERE RARITY = 'RARE')
ORDER BY A.ITEM_ID DESC;
```

* 서브쿼리
  * 해당 쿼리의 결과에서 데이터를 필터링, 검색, 조작하는 데 사용

### 10. 조건에 맞는 개발자 찾기
* DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요. 결과는 ID를 기준으로 오름차순 정렬해 주세요.

```SQL
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python')
    OR SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#')
ORDER BY ID ASC;
```

* 비트 연산자
  * & : 대응되는 비트가 모두 1이면 1반환
  * | : 대응되는 비트중 하나라도 1이면 1반환
  * ^ : 대응되는 비트가 서로 다르면 1반환
  * ~ : 비트가 1이면 0으로, 0이면 1로 반전
  * << : 왼쪽으로 이동
  * \>> : 오른쪽으로 이동 
* SKILL_CODE(b'110010000') & Python (b'100000000') -> 결과 100000000 -> 0이 아니므로 Python 스킬을 가지고 있다
* 동일한 방식으로 C# 스킬 포함여부도 검사
* OR 을 사용하여 Python과 C# 중 하나라도 포함된 결과 출력

### 11. 특정 물고기를 잡은 총 수 구하기
* FISH_INFO 테이블에서 잡은 BASS와 SNAPPER의 수를 출력하는 SQL 문을 작성해주세요. 컬럼명은 'FISH_COUNT`로 해주세요.

```SQL
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO AS A
INNER JOIN FISH_NAME_INFO AS B
ON A.FISH_TYPE = B.FISH_TYPE
WHERE B.FISH_NAME IN ('BASS', 'SNAPPER');
```

* IN
  * 조회하고자 하는 데이터 값이 여러개일 때, 목록을 만들어 조건 사용

### 12. 오프라인/온라인 판매 데이터 통합하기
* ONLINE_SALE 테이블과 OFFLINE_SALE 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력하는 SQL문을 작성해주세요. OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시해주세요. 결과는 판매일을 기준으로 오름차순 정렬해주시고 판매일이 같다면 상품 ID를 기준으로 오름차순, 상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬해주세요.

```SQL
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'

UNION

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'

ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;
```

* UNION
  * 쿼리의 결과를 합치고, 중복 결과는 제거
* UNION ALL
  * 쿼리의 결과를 합치고, 중복 결과도 포함 
* NULL AS 칼럼명
  * 해당 칼럼 모두 NULL 처리