-- SQLite
SELECT department_name, COUNT(*) as number_of_employees FROM employees
JOIN departments USING (department_id)
GROUP BY department_name
ORDER BY number_of_employees DESC


SELECT * FROM departments
SELECT * FROM employees