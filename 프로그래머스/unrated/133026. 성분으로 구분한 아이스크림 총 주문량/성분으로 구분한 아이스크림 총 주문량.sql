SELECT ice.INGREDIENT_TYPE, SUM(fh.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF AS fh
LEFT JOIN ICECREAM_INFO AS ice
    ON ice.FLAVOR = fh.FLAVOR
GROUP BY ice.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
