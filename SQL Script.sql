CREATE DATABASE phonepe;
USE phonepe;
CREATE TABLE aggregated_transaction(
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;
SELECT transaction_type, SUM(transaction_count) AS total
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total DESC;
SELECT year, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY year
ORDER BY year;
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10;
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10;
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10;
SELECT SUM(registered_users), SUM(app_opens)
FROM map_user;
SELECT year, SUM(insurance_amount) AS total
FROM aggregated_insurance
GROUP BY year;
SELECT entity_name, SUM(transaction_amount) AS total
FROM top_transaction
GROUP BY entity_name
ORDER BY total DESC
LIMIT 10;


