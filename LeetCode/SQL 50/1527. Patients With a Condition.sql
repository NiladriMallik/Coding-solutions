lSELECT
    PATIENT_ID,
    PATIENT_NAME,
    CONDITIONS
FROM PATIENTS
WHERE CONDITIONS LIKE 'DIAB1%' or CONDITIONS LIKE "% DIAB1%"
;