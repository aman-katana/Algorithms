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
