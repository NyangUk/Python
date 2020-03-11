-- SELECT 컬럼명, COUNT(*) FROM 테이블명 GROUP BY 컬럼명 HAVING COUNT(*)>1;
SELECT NAME ,COUNT(NAME) AS CNT
FROM ANIMAL_INS
GROUP BY NAME HAVING CNT>1
--그룹으로 묶었을때 NAME 항목에 있는 모든 이름을 카운ㅌ한뒤 having을 통해 조건을 달아준다.
