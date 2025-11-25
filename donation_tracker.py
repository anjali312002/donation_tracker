# donation_tracker.py

import sqlite3
from tkinter import *
from tkinter import messagebox

# ---------- Database Setup ----------
conn = sqlite3.connect("donations.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS donations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    item TEXT,
    quantity INTEGER,
    contact TEXT
)
""")
conn.commit()

# ---------- Functions ----------
def add_donation():
    name = name_entry.get()
    item = item_entry.get()
    qty = qty_entry.get()
    contact = contact_entry.get()

    if not (name and item and qty and contact):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    # Convert quantity to number
    try:
        qty = int(qty)
    except ValueError:
        messagebox.showwarning("Input Error", "Quantity must be a number")
        return

    cur.execute("INSERT INTO donations (name, item, quantity, contact) VALUES (?, ?, ?, ?)",
                (name, item, qty, contact))
    conn.commit()
    clear_fields()
    show_donations()
    update_summary()


def show_donations():
    listbox.delete(0, END)
    cur.execute("SELECT * FROM donations")
    rows = cur.fetchall()
    for row in rows:
        listbox.insert(END, f"ID:{row[0]} | {row[1]} donated {row[2]} ({row[3]}) | Contact: {row[4]}")
    update_summary()


def delete_donation():
    try:
        selected = listbox.get(listbox.curselection())
        donation_id = selected.split('|')[0].split(':')[1]
        cur.execute("DELETE FROM donations WHERE id=?", (donation_id,))
        conn.commit()
        show_donations()
        messagebox.showinfo("Deleted", "Donation removed successfully!")
        update_summary()
    except:
        messagebox.showwarning("Select Record", "Please select a donation to delete")


def clear_fields():
    name_entry.delete(0, END)
    item_entry.delete(0, END)
    qty_entry.delete(0, END)
    contact_entry.delete(0, END)


# ---------- New Function: Summary Dashboard ----------
def update_summary():
    cur.execute("SELECT COUNT(*), SUM(quantity) FROM donations")
    count, total_items = cur.fetchone()
    count = count if count else 0
    total_items = total_items if total_items else 0
    summary_label.config(
        text=f"🧾 Total Donations: {count}    |    🧺 Total Items Donated: {total_items}"
    )


# ---------- GUI Setup ----------
root = Tk()
root.title("🌍 Donation Tracker")
root.geometry("650x550")
root.config(bg="#f0f4f7")

# Title
Label(root, text="Donation Tracker", font=("Arial", 20, "bold"),
      bg="#f0f4f7", fg="#333").pack(pady=10)

# Input Frame
frame = Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

Label(frame, text="Name:", bg="#f0f4f7").grid(row=0, column=0, sticky=W, pady=2)
Label(frame, text="Item:", bg="#f0f4f7").grid(row=1, column=0, sticky=W, pady=2)
Label(frame, text="Quantity:", bg="#f0f4f7").grid(row=2, column=0, sticky=W, pady=2)
Label(frame, text="Contact:", bg="#f0f4f7").grid(row=3, column=0, sticky=W, pady=2)

name_entry = Entry(frame, width=40)
item_entry = Entry(frame, width=40)
qty_entry = Entry(frame, width=40)
contact_entry = Entry(frame, width=40)

name_entry.grid(row=0, column=1, padx=10)
item_entry.grid(row=1, column=1, padx=10)
qty_entry.grid(row=2, column=1, padx=10)
contact_entry.grid(row=3, column=1, padx=10)

# Buttons
btn_frame = Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add Donation", width=15, bg="#4CAF50", fg="white",
       command=add_donation).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Delete", width=15, bg="#f44336", fg="white",
       command=delete_donation).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Clear", width=15, bg="#2196F3", fg="white",
       command=clear_fields).grid(row=0, column=2, padx=5)

# Listbox to display donations
listbox = Listbox(root, width=80, height=15)
listbox.pack(pady=10)

# Summary Label (New)
summary_label = Label(root, text="", font=("Arial", 12, "bold"),
                      bg="#f0f4f7", fg="#333")
summary_label.pack(pady=10)

show_donations()
update_summary()

root.mainloop()
