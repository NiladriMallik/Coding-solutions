SELECT
    DISTINCT HOST.HOST_ID,
    GUEST.GUEST_ID
FROM AIRBNB_HOSTS HOST INNER JOIN AIRBNB_GUESTS GUEST
ON HOST.NATIONALITY = GUEST.NATIONALITY
AND HOST.GENDER = GUEST.GENDER
;