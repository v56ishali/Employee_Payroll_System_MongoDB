// ============================================================
//  APPLY MONGODB AGGREGATE FUNCTIONS TO
//  ANALYSE THE EMPLOYEE PAYROLL SYSTEM
// ============================================================

// ─────────────────────────────────────────────────────────
// STEP 1: Database and Collection (Simulated in Node.js)
// ─────────────────────────────────────────────────────────
const LINE  = "=".repeat(64);
const DASH  = "─".repeat(64);

console.log(LINE);
console.log("  Ex. No: 7  |  MONGODB AGGREGATE - EMPLOYEE PAYROLL SYSTEM");
console.log(LINE);
console.log();
console.log("Step 1: Create Database and Collection");
console.log("  > use payrollDB;");
console.log("  > db.createCollection('employees');");
console.log();

// ─────────────────────────────────────────────────────────
// STEP 2: Insert Sample Documents
// ─────────────────────────────────────────────────────────
console.log(DASH);
console.log("Step 2: Insert Sample Documents  (db.employees.insertMany([...]))");
console.log(DASH);

const employees = [
  { emp_id: "E101", name: "John",  department: "HR",      basic_salary: 45000, hra: 8000,  allowances: 3000 },
  { emp_id: "E102", name: "Mary",  department: "IT",      basic_salary: 60000, hra: 10000, allowances: 5000 },
  { emp_id: "E103", name: "Sam",   department: "Finance", basic_salary: 55000, hra: 9000,  allowances: 4000 },
  { emp_id: "E104", name: "David", department: "IT",      basic_salary: 65000, hra: 11000, allowances: 7000 },
  { emp_id: "E105", name: "Rose",  department: "HR",      basic_salary: 48000, hra: 8500,  allowances: 3500 },
];

console.log();
console.log(
  `  ${"Emp ID".padEnd(8)} ${"Name".padEnd(8)} ${"Department".padEnd(10)} ${"Basic Salary".padStart(14)} ${"HRA".padStart(8)} ${"Allowances".padStart(12)}`
);
console.log(
  `  ${"──────".padEnd(8)} ${"────".padEnd(8)} ${"──────────".padEnd(10)} ${"────────────".padStart(14)} ${"───────".padStart(8)} ${"──────────".padStart(12)}`
);
for (const e of employees) {
  console.log(
    `  ${e.emp_id.padEnd(8)} ${e.name.padEnd(8)} ${e.department.padEnd(10)} ${e.basic_salary.toLocaleString().padStart(14)} ${e.hra.toLocaleString().padStart(8)} ${e.allowances.toLocaleString().padStart(12)}`
  );
}
console.log();
console.log("  ✔  5 documents inserted successfully.");
console.log();

// ─────────────────────────────────────────────────────────
// STEP 3: Aggregate Queries
// ─────────────────────────────────────────────────────────
console.log(LINE);
console.log("Step 3: Apply Aggregate Queries");
console.log(LINE);

// ── i. Total Salary of Each Employee ──────────────────────
console.log();
console.log("i. Calculate Total Salary of Each Employee");
console.log(DASH);
console.log(`   db.employees.aggregate([
     {
       $project: {
         name: 1,
         department: 1,
         total_salary: { $sum: ["$basic_salary", "$hra", "$allowances"] }
       }
     }
   ]);`);
console.log();
console.log("  Output:");
console.log(
  `  ${"Name".padEnd(8)} ${"Department".padEnd(12)} ${"Total Salary".padStart(14)}`
);
console.log(
  `  ${"──────".padEnd(8)} ${"──────────".padEnd(12)} ${"────────────".padStart(14)}`
);
for (const e of employees) {
  const total = e.basic_salary + e.hra + e.allowances;
  console.log(
    `  ${e.name.padEnd(8)} ${e.department.padEnd(12)} ${total.toLocaleString().padStart(14)}`
  );
}

// ── ii. Total Salary Paid by the Organisation ─────────────
console.log();
console.log(DASH);
console.log("ii. Find Total Salary Paid by the Organization");
console.log(DASH);
console.log(`   db.employees.aggregate([
     {
       $group: {
         _id: "Total Salary",
         total_paid: {
           $sum: { $sum: ["$basic_salary", "$hra", "$allowances"] }
         }
       }
     }
   ]);`);
console.log();
const orgTotal = employees.reduce(
  (acc, e) => acc + e.basic_salary + e.hra + e.allowances, 0
);
console.log("  Output:");
console.log(`  ${"_id".padEnd(20)} ${"total_paid".padStart(14)}`);
console.log(`  ${"──────────────────".padEnd(20)} ${"────────────".padStart(14)}`);
console.log(`  ${"Total Salary".padEnd(20)} ${orgTotal.toLocaleString().padStart(14)}`);

// ── iii. Department-wise Average Basic Salary ──────────────
console.log();
console.log(DASH);
console.log("iii. Department-wise Average Salary");
console.log(DASH);
console.log(`   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         avg_basic_salary: { $avg: "$basic_salary" }
       }
     }
   ]);`);
console.log();
const deptSalary = {};
for (const e of employees) {
  if (!deptSalary[e.department]) deptSalary[e.department] = [];
  deptSalary[e.department].push(e.basic_salary);
}
console.log("  Output:");
console.log(
  `  ${"_id (Department)".padEnd(18)} ${"avg_basic_salary".padStart(18)}`
);
console.log(
  `  ${"────────────────".padEnd(18)} ${"────────────────".padStart(18)}`
);
for (const dept of Object.keys(deptSalary).sort()) {
  const salaries = deptSalary[dept];
  const avg = salaries.reduce((a, b) => a + b, 0) / salaries.length;
  console.log(`  ${dept.padEnd(18)} ${avg.toFixed(2).padStart(18)}`);
}

// ── iv. Highest and Lowest Salary in Each Dept ────────────
console.log();
console.log(DASH);
console.log("iv. Highest and Lowest Salary in Each Department");
console.log(DASH);
console.log(`   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         max_salary: { $max: "$basic_salary" },
         min_salary: { $min: "$basic_salary" }
       }
     }
   ]);`);
console.log();
console.log("  Output:");
console.log(
  `  ${"_id (Department)".padEnd(16)} ${"max_salary".padStart(12)} ${"min_salary".padStart(12)}`
);
console.log(
  `  ${"────────────────".padEnd(16)} ${"──────────".padStart(12)} ${"──────────".padStart(12)}`
);
for (const dept of Object.keys(deptSalary).sort()) {
  const salaries = deptSalary[dept];
  const maxS = Math.max(...salaries);
  const minS = Math.min(...salaries);
  console.log(
    `  ${dept.padEnd(16)} ${maxS.toLocaleString().padStart(12)} ${minS.toLocaleString().padStart(12)}`
  );
}

// ── v. Count Employees in Each Department ─────────────────
console.log();
console.log(DASH);
console.log("v. Count Number of Employees in Each Department");
console.log(DASH);
console.log(`   db.employees.aggregate([
     {
       $group: {
         _id: "$department",
         emp_count: { $count: {} }
       }
     }
   ]);`);
console.log();
const deptCount = {};
for (const e of employees) {
  deptCount[e.department] = (deptCount[e.department] || 0) + 1;
}
console.log("  Output:");
console.log(
  `  ${"_id (Department)".padEnd(18)} ${"emp_count".padStart(12)}`
);
console.log(
  `  ${"────────────────".padEnd(18)} ${"─────────".padStart(12)}`
);
for (const dept of Object.keys(deptCount).sort()) {
  console.log(`  ${dept.padEnd(18)} ${String(deptCount[dept]).padStart(12)}`);
}

// ── vi. Sort Employees by Salary Descending ───────────────
console.log();
console.log(DASH);
console.log("vi. Sort Employees by Salary (Descending)");
console.log(DASH);
console.log(`   db.employees.aggregate([
     { $sort: { basic_salary: -1 } }
   ]);`);
console.log();
const sorted = [...employees].sort((a, b) => b.basic_salary - a.basic_salary);
console.log("  Output:");
console.log(
  `  ${"Emp ID".padEnd(8)} ${"Name".padEnd(8)} ${"Department".padEnd(12)} ${"Basic Salary".padStart(14)}`
);
console.log(
  `  ${"──────".padEnd(8)} ${"────".padEnd(8)} ${"──────────".padEnd(12)} ${"────────────".padStart(14)}`
);
for (const e of sorted) {
  console.log(
    `  ${e.emp_id.padEnd(8)} ${e.name.padEnd(8)} ${e.department.padEnd(12)} ${e.basic_salary.toLocaleString().padStart(14)}`
  );
}

// ─────────────────────────────────────────────────────────
console.log();
console.log(LINE);
console.log("  ✔  All MongoDB Aggregate Queries Executed Successfully!");
console.log(LINE);
