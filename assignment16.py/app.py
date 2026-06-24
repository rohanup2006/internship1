import os
from pyspark import SparkConf, SparkContext

def parse_csv(line):
    parts = line.split(',')
    return int(parts[0]), parts[1], parts[2], int(parts[3])

def main():
    conf = SparkConf().setAppName("EmployeeRDDApp").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    sc.setLogLevel("ERROR")

    # Read CSV
    data = sc.textFile("employees.csv")

    # Remove header
    header = data.first()
    records = data.filter(lambda x: x != header).map(parse_csv)

    # 1. SORT EMPLOYEES BY SALARY
    sorted_emps = records.sortBy(lambda x: x[3], ascending=False)

    print("\n=== Employees Sorted by Salary (Descending) ===")
    for emp in sorted_emps.collect():
        print(emp)

    # 2. DEPARTMENT-WISE TOTAL SALARY
    dept_totals = records.map(lambda x: (x[2], x[3])) \
                         .reduceByKey(lambda a, b: a + b)

    print("\n=== Department-wise Total Salary ===")
    for dept, total in dept_totals.collect():
        print(f"Department: {dept} -> {total}")

    # 3. TOP 3 EMPLOYEES (SAVE TO FILE)
    top3 = sorted_emps.take(3)

    os.makedirs("output", exist_ok=True)

    with open("output/top3_employees.txt", "w") as f:
        f.write("Top 3 Highest Paid Employees:\n")
        for emp in top3:
            f.write(f"ID: {emp[0]} | Name: {emp[1]} | Dept: {emp[2]} | Salary: {emp[3]}\n")

    print("\nTop 3 employees saved to output/top3_employees.txt")

    sc.stop()

if __name__ == "__main__":
    main()