# 175. Combine Two Tables
# SELECT firstName, lastName, city, state
# FROM Person
# LEFT JOIN Address ON Person.personID = Address.personID


# 176. Second Highest Salary
# WITH CTE_Salaries AS(
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY salary DESC
#     LIMIT 1, 1
# )
# SELECT IF(COUNT(salary)=1, salary, null) AS SecondHighestSalary
# FROM CTE_Salaries


# 178. Rank Scores
# SELECT score,
# DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
# FROM Scores


# 181. Employees Earning More Than Their Managers
# SELECT emp1.name as 'Employee'
# FROM Employee AS emp1
# LEFT JOIN Employee AS emp2
#     ON emp1.managerId = emp2.id
# WHERE emp1.salary > emp2.salary;


# 182. Duplicate Emails
# SELECT email AS Email
# FROM Person
# GROUP BY email
# HAVING COUNT(Email) > 1


# 183. Customers Who Never Order
# SELECT Customers.name AS Customers
# FROM Customers
# WHERE Customers.id NOT IN (
#     SELECT DISTINCT customerId
#     FROM  Orders
# )


# 185. Department Top Three Salaries
# WITH CTE_Rank(Department, Employee, Salary, rn)  AS(
#     SELECT
#         D.name, E.name, E.salary,
#         DENSE_RANK() OVER(PARTITION BY E.departmentId ORDER BY E.salary DESC) AS rn
#     FROM Employee E
#     JOIN Department D
#         ON E.departmentId = D.id
#
# )SELECT Department, Employee, Salary
# FROM CTE_Rank
# WHERE rn < 4


# 196. Delete Duplicate Emails
# DELETE P1
# FROM Person AS P1
# JOIN Person AS P2
# WHERE P1.email = P2.email AND P1.id > P2.id


# 197. Rising Temperature
# SELECT W1.id
# FROM Weather AS W1
# INNER JOIN Weather AS W2
#     ON DATEDIFF(W1.recordDate, W2.recordDate) = 1
# WHERE W1.temperature > W2.temperature


# 184. Department Highest Salary
# WITH CTE_ranked(Department, Employee, Salary, rn) AS (
#     SELECT
#     D.name, E.name, E.salary,
#     DENSE_RANK() OVER(PARTITION BY E.departmentId ORDER BY salary DESC) AS rn
#
# FROM Employee E
# JOIN Department D
#     ON E.departmentId = D.id
#
# )SELECT Department, Employee, Salary
# FROM CTE_ranked
# WHERE rn = 1


# 511. Game Play Analysis I
# SELECT player_id, MIN(event_date) AS first_login
# FROM Activity
# GROUP BY player_id
