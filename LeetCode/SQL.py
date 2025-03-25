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
