Departments
-
dept_no varchar pk
dept_name varchar

Employees
-
emp_no int pk
birth_date date
first_name varchar
last_name varchar
gender varchar
hire_date date

Managers
-
dept_no varchar pk fk - Departments.dept_no
emp_no int pk fk - Employees.emp_no
from_date date
to_date date

Dept_Emp
-
emp_no int pk fk -< Employees.emp_no
dept_no varchar pk fk -< Departments.dept_no
from_date date
to_date date

Salaries
-
emp_no int pk fk - Employees.emp_no
salary int
from_date date
to_date date


Titles
-
emp_no int pk fk -< Employees.emp_no
title varchar pk
from_date date pk
to_date date