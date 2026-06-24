import sqlite3

# CREATE DATABASE   
    
conn = sqlite3.connect("sqlite1.db")
# CREATE TABLE

conn.execute('''
CREATE TABLE IF NOT EXISTS student(
    st_id INTEGER PRIMARY KEY AUTOINCREMENT,
    st_nm VARCHAR(50),
    st_class VARCHAR(20),
    st_email VARCHAR(80)
)
''')
# INSERT RECORDS

conn.execute("""
INSERT INTO student(st_nm, st_class, st_email)
VALUES('Rahul', 'BCA', 'rahul@gmail.com')
""")

conn.execute("""
INSERT INTO student(st_nm, st_class, st_email)
VALUES('Priya', 'BBA', 'priya@gmail.com')
""")

conn.execute("""
INSERT INTO student(st_nm, st_class, st_email)
VALUES('Aman', 'MCA', 'aman@gmail.com')
""")

conn.commit()

print("Records inserted successfully!")

# SELECT ALL RECORDS

print("\nAll Student Records:")

cursor = conn.execute("SELECT * FROM student")

for row in cursor:
    print(row)


# SELECT ONLY NAMES


print("\nStudent Names:")

cursor = conn.execute("SELECT st_nm FROM student")

for row in cursor:
    print(row)


# SELECT USING WHERE


print("\nStudents from BCA Class:")

cursor = conn.execute("""
SELECT * FROM student
WHERE st_class = 'BCA'
""")

for row in cursor:
    print(row)


# SELECT USING ORDER BY


print("\nStudents Sorted by Name:")

cursor = conn.execute("""
SELECT * FROM student
ORDER BY st_nm
""")

for row in cursor:
    print(row)


# UPDATE RECORD


conn.execute("""
UPDATE student
SET st_class = 'MBA'
WHERE st_id = 2
""")

conn.commit()

# DELETE RECORD


conn.execute("""
DELETE FROM student
WHERE st_id = 3
""")

conn.commit()
conn.close()