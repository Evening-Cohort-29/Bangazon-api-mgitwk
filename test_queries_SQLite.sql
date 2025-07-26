-- SQLite

-- retrieve table names
.tables

-- query test for ticket 26
SELECT
    o.id AS order_id,
    u.first_name || ' ' || u.last_name AS customer_name,
    SUM(p.price) AS total_cost
FROM bangazonapi_order o
JOIN bangazonapi_orderproduct op ON o.id = op.order_id
JOIN bangazonapi_product p ON op.product_id = p.id
JOIN bangazonapi_customer c ON o.customer_id = c.id
JOIN auth_user u ON c.user_id = u.id
WHERE o.payment_type_id IS NULL
GROUP BY o.id, u.first_name, u.last_name
ORDER BY o.id;
