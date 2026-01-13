-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, CASE RTRIM(UPPER(SEX_UPON_INTAKE), ' FMALE')
                                  WHEN 'NEUTERED' THEN 'O' 
                                  WHEN 'SPAYED' THEN 'O'
                                  ELSE 'X' END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID