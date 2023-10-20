## [프로그래머스 / SQL]

- 조건별로 분류하여 주문상태 출력하기

  ```sql
  SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
  CASE
      WHEN OUT_DATE <= '20220501'
          THEN '출고완료'
      WHEN OUT_DATE > '20220501'
          THEN '출고대기'
      ELSE '출고미정'
      END AS '출고여부'
  FROM FOOD_ORDER
  ORDER BY ORDER_ID;
  ```

- 주문량이 많은 아이스크림들 조회하기

  ```sql
  SELECT F.FLAVOR FROM FIRST_HALF F
  JOIN JULY AS J
  ON F.FLAVOR = J.FLAVOR
  GROUP BY F.FLAVOR
  ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC LIMIT 3;
  ```

  