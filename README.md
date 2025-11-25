Here you go — FULL README content in one block for direct copy-paste:

---

```
# 🧾 Donation Tracker

Donation Tracker is a simple Python application built using **SQLite3** and **Tkinter** for tracking donations made by individuals. It allows users to enter and store donor details and view stored donation records through a graphical interface.

---

## ✨ Features

✔ Add donor information  
✔ Store donations in an SQLite database  
✔ View donation records via GUI  
✔ Automatic table creation  
✔ Lightweight and easy to use  
✔ No external dependencies

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Database | SQLite3 |
| GUI | Tkinter |

---

## 📂 Project Structure

```

donation_tracker/
│
├── donation_tracker.py      # Main application
├── view_database.py         # View donations window
├── donations.db             # SQLite database file
└── README.md                # This file

```

---

## ▶️ How to Run

### 1️⃣ Make sure you have Python installed

Check with:

```

python --version

```

or

```

python3 --version

```

---

### 2️⃣ Run the main application

```

python donation_tracker.py

```

or

```

python3 donation_tracker.py

```

---

## 🧩 Usage

- Enter donor name  
- Enter item donated  
- Enter quantity  
- Enter contact number  
- Submit the donation  
- Click “View Database” to see stored records

---

## 💾 Database

This project uses **SQLite**, and if `donations.db` does not exist, it is automatically created with this schema:

```

id INTEGER PRIMARY KEY AUTOINCREMENT
name TEXT
item TEXT
quantity INTEGER
contact TEXT

```

---

## 👤 Author

**Anjali Sharma**  
GitHub: https://github.com/anjali312002  
Email: anjalisharma312002@gmail.com

---


Just paste this into your `README.md` in VS Code 🙌
