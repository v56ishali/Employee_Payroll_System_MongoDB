"""
============================================================
  APPLY MONGODB AGGREGATE FUNCTIONS TO
  ANALYSE THE EMPLOYEE PAYROLL SYSTEM
============================================================
  This script simulates MongoDB aggregate queries on an
  Employee Payroll collection and displays formatted output.
============================================================
"""

from collections import defaultdict

# ─────────────────────────────────────────────────────────
# STEP 1: Database and Collection (Simulated)
# ─────────────────────────────────────────────────────────
print("=" * 62)
print("  Copyright2026  |  EMPLOYEE PAYROLL SYSTEM - MONGODB AGGREGATION")
print("=" * 62)
print()
print("Step 1: Create Database and Collection")
print("  use payrollDB;")
print("  db.createCollection('employees');")
print()

# ─────────────────────────────────────────────────────────
# STEP 2: Insert Sample Documents
# ─────────────────────────────────────────────────────────
print("─" * 62)
print("Step 2: Insert Sample Documents")
print("─" * 62)

employees = [
    {"emp_id": "E101", "name": "John",  "department": "HR",      "basic_salary": 45000, "hra": 8000,  "allowances": 3000},
    {"emp_id": "E102", "name": "Mary",  "department": "IT",      "basic_salary": 60000, "hra": 10000, "allowances": 5000},
    {"emp_id": "E103", "name": "Sam",   "department": "Finance", "basic_salary": 55000, "hra": 9000,  "allowances": 4000},
    {"emp_id": "E104", "name": "David", "department": "IT",      "basic_salary": 65000, "hra": 11000, "allowances": 7000},
    {"emp_id": "E105", "name": "Rose",  "department": "HR",      "basic_salary": 48000, "hra": 8500,  "allowances": 3500},
]

print()
print(f"  {'Emp ID':<8} {'Name':<8} {'Department':<10} {'Basic Salary':>13} {'HRA':>8} {'Allowances':>12}")
print(f"  {'─'*6:<8} {'─'*6:<8} {'─'*10:<10} {'─'*12:>13} {'─'*6:>8} {'─'*10:>12}")
for e in employees:
    print(f"  {e['emp_id']:<8} {e['name']:<8} {e['department']:<10} {e['basic_salary']:>13,} {e['hra']:>8,} {e['allowances']:>12,}")
print()
print("  ✔ db.employees.insertMany([...]) — 5 documents inserted.")
print()

# ─────────────────────────────────────────────────────────
# STEP 3: Aggregate Queries
# ─────────────────────────────────────────────────────────
print("=" * 62)
print("Step 3: Apply Aggregate Queries")
print("=" * 62)

# ── Query i: Total Salary of Each Employee ──────────────
print()
print("i. Calculate Total Salary of Each Employee")
print("─" * 62)
print("""   db.employees.aggregate([
     {
       $project: {
         name: 1,
         department: 1,
         total_salary: { $sum: ["$basic_salary", "$hra", "$allowances"] }
       }
     }
   ]);""")
print()
print("  Output:")
print(f"  {'Name':<8} {'Department':<12} {'Total Salary':>14}")
print(f"  {'─'*6:<8} {'─'*10:<12} {'─'*12:>14}")
for e in employees:
    total = e["basic_salary"] + e["hra"] + e["allowances"]
    print(f"  {e['name']:<8} {e['department']:<12} {total:>14,}")

# ── Query ii: Total Salary Paid by the Organisation ─────
print()
print("─" * 62)
print("ii. Find Total Salary Paid by the Organization")
print("─" * 62)
print("""   db.employees.aggregate([
     {
       $group: {
         _id: "Total Salary",
         total_paid: {
           $sum: { $sum: ["$basic_salary", "$hra", "$allowances"] }
         }
       }
     }
   ]);""")
print()
org_total = sum(e["basic_salary"] + e["hra"] + e["allowances"] for e in employees)
print("  Output:")
print(f"  {'_id':<20} {'total_paid':>14}")
print(f"  {'─'*18:<20} {'─'*12:>14}")
print(f"  {'Total Salary':<20} {org_total:>14,}")

# ── Query iii: Department-wise Average Basic Salary ──────
print()
print("─" * 62)
print("iii. Department-wise Average Salary")
print("─" * 62)
print("""   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         avg_basic_salary: { $avg: "$basic_salary" }
       }
     }
   ]);""")
print()
dept_salary = defaultdict(list)
for e in employees:
    dept_salary[e["department"]].append(e["basic_salary"])

print("  Output:")
print(f"  {'_id (Department)':<18} {'avg_basic_salary':>18}")
print(f"  {'─'*16:<18} {'─'*16:>18}")
for dept, salaries in sorted(dept_salary.items()):
    avg = sum(salaries) / len(salaries)
    print(f"  {dept:<18} {avg:>18,.2f}")

# ── Query iv: Highest and Lowest Salary in Each Dept ────
print()
print("─" * 62)
print("iv. Highest and Lowest Salary in Each Department")
print("─" * 62)
print("""   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         max_salary: { $max: "$basic_salary" },
         min_salary: { $min: "$basic_salary" }
       }
     }
   ]);""")
print()
print("  Output:")
print(f"  {'_id (Department)':<16} {'max_salary':>12} {'min_salary':>12}")
print(f"  {'─'*15:<16} {'─'*10:>12} {'─'*10:>12}")
for dept, salaries in sorted(dept_salary.items()):
    print(f"  {dept:<16} {max(salaries):>12,} {min(salaries):>12,}")

# ── Query v: Count Number of Employees in Each Dept ─────
print()
print("─" * 62)
print("v. Count Number of Employees in Each Department")
print("─" * 62)
print("""   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         emp_count: { $count: {} }
       }
     }
   ]);""")
print()
dept_count = defaultdict(int)
for e in employees:
    dept_count[e["department"]] += 1

print("  Output:")
print(f"  {'_id (Department)':<18} {'emp_count':>12}")
print(f"  {'─'*16:<18} {'─'*10:>12}")
for dept, count in sorted(dept_count.items()):
    print(f"  {dept:<18} {count:>12}")

# ── Query vi: Sort Employees by Salary (Descending) ──────
print()
print("─" * 62)
print("vi. Sort Employees by Salary (Descending)")
print("─" * 62)
print("""   db.employees.aggregate([
     { $sort: { basic_salary: -1 } }
   ]);""")
print()
sorted_emps = sorted(employees, key=lambda x: x["basic_salary"], reverse=True)
print("  Output:")
print(f"  {'Emp ID':<8} {'Name':<8} {'Department':<12} {'Basic Salary':>14}")
print(f"  {'─'*6:<8} {'─'*6:<8} {'─'*10:<12} {'─'*12:>14}")
for e in sorted_emps:
    print(f"  {e['emp_id']:<8} {e['name']:<8} {e['department']:<12} {e['basic_salary']:>14,}")

# ─────────────────────────────────────────────────────────
print()
print("=" * 62)
print("  ✔  All MongoDB Aggregate Queries Executed Successfully!")
print("=" * 62)
