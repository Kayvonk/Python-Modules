# Module 03: Databases and SQL with SQLite 🗄️

## 🧠 Overview
In this module, you'll learn about **databases** and how to use **SQL** (Structured Query Language) to store, retrieve, and manage data. We'll use **SQLite**, a simple, file-based database that works well for beginners and integrates easily with Python. You'll also see how to connect SQLite with Flask to build backend apps with persistent storage.

This module is essential for understanding how backend web development handles data behind the scenes.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand what a database is and why it’s important  
- Learn basic SQL commands: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`  
- Use Python’s `sqlite3` module to interact with SQLite databases  
- Prevent SQL injection attacks using parameterized queries  
- Connect Flask apps to SQLite for persistent backend storage  
- Build a small backend project combining Flask and SQLite  

---

## 🧩 Exercises

| Filename                      | Description                                           |
|------------------------------|-------------------------------------------------------|
| 01_introduction_to_databases.py | What is a database and why use it?                   |
| 02_install_and_setup_sqlite.py  | Setup SQLite and Python’s sqlite3 module             |
| 03_create_table.py             | Create a table with SQL                               |
| 04_insert_data.py              | Insert records into your table                        |
| 05_query_data.py               | Select and display data                               |
| 06_update_and_delete.py        | Update and delete records                             |
| 07_prevent_sql_injection.py    | Secure your queries with parameterized inputs         |
| 08_sqlite_flask_integration.py | Use SQLite in a Flask app                             |
| 09_mini_project_todo_app.py    | Build a simple To-Do list backend with Flask + SQLite |

---

## 🏁 End-of-Module Challenge

🎯 **Mini Project: To-Do List Backend**  
Build a Flask app connected to SQLite that lets users:  
- **Create** tasks  
- **View** all tasks  
- **Update** tasks  
- **Delete** tasks  

The data should persist between server restarts and use JSON for requests and responses.

---