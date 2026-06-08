SELECT s.customer_id,
       SUM(m.price) AS total_amount
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;
-----------------------------------------------------------------------------------------------------------------------------------
SELECT customer_id,
       COUNT(DISTINCT order_date) AS visit_days
FROM sales
GROUP BY customer_id;
-----------------------------------------------------------------------------------------------------------------------------------
SELECT customer_id,order_date, product_name
from sales s
inner join menu m
ON s.product_id = m.product_id
order by order_date
-----------------------------------------------------------------------------------------------------------------------------------
SELECT TOP 1
       m.product_name,
       COUNT(*) AS purchase_count
FROM sales s
inner JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY purchase_count DESC;
-----------------------------------------------------------------------------------------------------------------------------------


