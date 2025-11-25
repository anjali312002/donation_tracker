import sqlite3

# Connect to the same database your app uses
conn = sqlite3.connect("donations.db")
cur = conn.cursor()

cur.execute("SELECT * FROM donations")
rows = cur.fetchall()

print("\n🧾 DONATION RECORDS:\n")
print("ID | Name | Item | Quantity | Contact")
print("-" * 60)

for row in rows:
    print(row)

conn.close()
