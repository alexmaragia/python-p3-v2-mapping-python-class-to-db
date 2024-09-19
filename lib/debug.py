#!/usr/bin/env python3
#lib/debug.py

from __init__ import CONN, CURSOR
from department import Department
import ipdb

# Drop and recreate the table
Department.drop_table()
Department.create_table()

# Create departments using the create method
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # Should print: <Department 1: Payroll, Building A, 5th Floor>

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # Should print: <Department 2: Human Resources, Building C, East Wing>

# Update a department
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # Should print: <Department 2: HR, Building F, 10th Floor>

# Delete a department
print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # Should print: <Department 1: Payroll, Building A, 5th Floor>

# Start an interactive debugging session
ipdb.set_trace()