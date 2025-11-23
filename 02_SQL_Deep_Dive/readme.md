<!-- CONCEPT OF CASE -->
# LEARNING SQL

## SQL CASE

```sql
CASE 
WHEN condition THEN result
WHEN condition THEN result
ELSE final_result
END
```

# QUESTION

**Business Question:** Using the payments table, categorize all orders as **'High Value'** (payment value over R200), **'Medium Value'** (R50 to R200),or **'LowValue'** (underR50).

<details>
  <summary>Click fro Answer</summary>

```
SELECT
    a.*,
    CASE
        WHEN a.payment_value > 200 THEN 'High Value'
        WHEN a.payment_value >= 50 AND a.payment_value <= 200 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS SEGMENT
FROM
    order_payments AS a;
```
</details>

## AGGRIGATION ON SEGMENTS

### CTE's


