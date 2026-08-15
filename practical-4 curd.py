import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("students.db")

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# CREATE - Insert data
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ("Deep", 18, "Computer Engineering")
)

connection.commit()

print("CREATE: Student added successfully.")

# READ - Display data
print("\nREAD: Student Records")

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# UPDATE - Update data
cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    ("Deep Chavda", 1)
)

connection.commit()

print("\nUPDATE: Student updated successfully.")

# READ again
cursor.execute("SELECT * FROM students")

print("\nREAD: Updated Student Records")

for row in cursor.fetchall():
    print(row)

# DELETE - Delete data
cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (1,)
)

connection.commit()

print("\nDELETE: Student deleted successfully.")

# Close connection
connection.close()

print("\nDatabase connection closed.")  
