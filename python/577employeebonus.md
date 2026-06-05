# Write your MySQL query statement below
SELECT name, bonus
FROM Employee
INNER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL;