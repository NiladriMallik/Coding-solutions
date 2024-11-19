-- Write your MySQL query statement below
SELECT
X, Y, Z,
CASE
    WHEN ((X + Y > Z) AND (X + Z > Y)) AND 
    ((Y + Z > X) AND (Y + X > Z)) AND
    ((Z + Y > X) AND (Z + X > Y)) THEN "Yes"
    ELSE "No"
END AS TRIANGLE
FROM TRIANGLE
;