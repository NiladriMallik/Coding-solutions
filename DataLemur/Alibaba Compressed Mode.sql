--PostgreSQL

SELECT ITEM_COUNT AS MODE FROM ITEMS_PER_ORDER
WHERE ORDER_OCCURRENCES =
(
  SELECT
    MAX(ORDER_OCCURRENCES)
  FROM ITEMS_PER_ORDER
)
;