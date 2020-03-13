SELECT
    ANIMAL_ID,
    NAME,    
    case
        when (SEX_UPON_INTAKE Like'%Neutered%') then 'O'
        when (SEX_UPON_INTAKE Like'%Spayed%') then 'O'
        else 'X'
    end as '중성화'
from ANIMAL_INS ;

-- WHEN 조건1 THEN 실행문1 WNEN 조건2 THEN 실행문 2ELSE 실행문 3
-- if 조건1: 실행문1 elif 조건2 :실행문2 else: 실행문3