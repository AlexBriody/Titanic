-- Count how many rows you have
SELECT COUNT(*) -- Counts all rows from...
FROM titanic;

-- How many people survived?
SELECT COUNT(*) -- Counts all rows from/where...
FROM titanic 
WHERE survived = 1; -- Filters rows where survived column is = 1 (true)

-- What passenger class has the largest population?
SELECT pclass, COUNT(*) AS population --Selecting pclass column and counting all rows for each pclass as population
FROM titanic 
GROUP BY pclass -- Grouping the rows by the same pclass
ORDER BY population DESC -- Sorts the population in descending order
LIMIT 1; -- Limits the result to only one row, so the first row will be the highest count
