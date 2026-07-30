
-- Customer Segmentation SQL Queries


-- 1. Display all customers
SELECT * FROM customers;

-- 2. Total number of customers
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- 3. Average age
SELECT ROUND(AVG(Age),2) AS Average_Age
FROM customers;

-- 4. Average annual income
SELECT ROUND(AVG(AnnualIncome),2) AS Average_Annual_Income
FROM customers;

-- 5. Average spending score
SELECT ROUND(AVG(SpendingScore),2) AS Average_Spending_Score
FROM customers;

-- 6. Customers by gender
SELECT Gender,
COUNT(*) AS Customer_Count
FROM customers
GROUP BY Gender;

-- 7. Customers by cluster
SELECT Cluster,
COUNT(*) AS Customer_Count
FROM customers
GROUP BY Cluster
ORDER BY Cluster;

-- 8. Average income by cluster
SELECT Cluster,
ROUND(AVG(AnnualIncome),2) AS Average_Income
FROM customers
GROUP BY Cluster;

-- 9. Average spending score by cluster
SELECT Cluster,
ROUND(AVG(SpendingScore),2) AS Average_Spending
FROM customers
GROUP BY Cluster;

-- 10. Average age by cluster
SELECT Cluster,
ROUND(AVG(Age),2) AS Average_Age
FROM customers
GROUP BY Cluster;

-- 11. Highest annual income
SELECT MAX(AnnualIncome) AS Highest_Income
FROM customers;

-- 12. Lowest annual income
SELECT MIN(AnnualIncome) AS Lowest_Income
FROM customers;

-- 13. Highest spending score
SELECT MAX(SpendingScore) AS Highest_Spending
FROM customers;

-- 14. Lowest spending score
SELECT MIN(SpendingScore) AS Lowest_Spending
FROM customers;

-- 15. Customers aged above 40
SELECT *
FROM customers
WHERE Age > 40;

-- 16. High income customers
SELECT *
FROM customers
WHERE AnnualIncome > 70;

-- 17. High spending customers
SELECT *
FROM customers
WHERE SpendingScore > 80;

-- 18. Female customers
SELECT COUNT(*) AS Female_Customers
FROM customers
WHERE Gender='Female';

-- 19. Male customers
SELECT COUNT(*) AS Male_Customers
FROM customers
WHERE Gender='Male';

-- 20. Top 10 customers by spending score
SELECT *
FROM customers
ORDER BY SpendingScore DESC
LIMIT 10;