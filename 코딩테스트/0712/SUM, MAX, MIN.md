### 1. 가격이 제일 비싼 식품의 정보 출력하기
* FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.

```SQL
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
```
```SQL
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
```

* 서브쿼리로 조건 만들기
* 또는 LIMIT 사용해서 최고값 출력

### 2. 가장 비싼 상품 구하기
* PRODUCT 테이블에서 판매 중인 상품 중 가장 높은 판매가를 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 MAX_PRICE로 지정해주세요.

```SQL
SELECT PRICE AS MAX_PRICE
FROM PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM PRODUCT)
```

### 3. 최댓값 구하기
* 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

```SQL
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
```

### 4. 최솟값 구하기
* 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

```SQL
SELECT DATETIME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)
```

### 5. 동물 수 구하기
* 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

```SQL
SELECT COUNT(ANIMAL_ID) FROM ANIMAL_INS
```

### 6. 중복 제거하기
* 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

```SQL
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
```

* DISTINCT 로 중복 제거
* COUNT시에 NULL 데이터는 포함 X

### 7. 조건에 맞는 아이템들의 가격의 총합 구하기
* ITEM_INFO 테이블에서 희귀도가 'LEGEND'인 아이템들의 가격의 총합을 구하는 SQL문을 작성해 주세요. 이때 컬럼명은 'TOTAL_PRICE'로 지정해 주세요.

```SQL
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY = 'LEGEND'
```

### 8. 물고기 종류 별 대어 찾기
* 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력하는 SQL 문을 작성해주세요. 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH로 해주세요. 결과는 물고기의 ID에 대해 오름차순 정렬해주세요. 단, 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 이하의 물고기가 가장 큰 경우는 없습니다.

```SQL
SELECT A.ID, B.FISH_NAME, A.LENGTH
FROM FISH_INFO AS A
INNER JOIN FISH_NAME_INFO AS B
ON A.FISH_TYPE = B.FISH_TYPE
WHERE A.FISH_TYPE IN (
    SELECT FISH_TYPE 
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING LENGTH = MAX(LENGTH)
)
ORDER BY ID ASC;
```

* 서브쿼리와 IN 활용
* GROUP BY와 HAVING 절로 조건

### 9. 잡은 물고기 중 가장 큰 물고기의 길이 구하기
* FISH_INFO 테이블에서 잡은 물고기 중 가장 큰 물고기의 길이를 'cm' 를 붙여 출력하는 SQL 문을 작성해주세요. 이 때 컬럼명은 'MAX_LENGTH' 로 지정해주세요.

```SQL
SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO
```

* CONCAT( , ) 활용하여 문자열 합치기

### 10. 연도별 대장균 크기의 편차 구하기
* 분화된 연도(YEAR), 분화된 연도별 대장균 크기의 편차(YEAR_DEV), 대장균 개체의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 분화된 연도별 대장균 크기의 편차는 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기로 구하며 결과는 연도에 대해 오름차순으로 정렬하고 같은 연도에 대해서는 대장균 크기의 편차에 대해 오름차순으로 정렬해주세요.

```SQL
SELECT YEAR(A.DIFFERENTIATION_DATE) AS YEAR, B.MAX_SIZE - A.SIZE_OF_COLONY AS YEAR_DEV, A.ID 
FROM ECOLI_DATA AS A
INNER JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR
) AS B
ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC;
```

* 서브쿼리 활용 -> 연도별 최대 값 구해야하므로
  * GROUP BY YEAR
* 해당 서브쿼리를 JOIN 하여 연도별 최대값 가져오기