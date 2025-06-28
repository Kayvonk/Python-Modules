# Module 03: Building APIs with Flask 🌐

## 🧠 Overview
In this module, you'll turn your Python code into a **web server** using a tool called **Flask**. Instead of printing things in the terminal, your code will be able to send and receive data over the internet! You’ll learn how to build a simple **API** — a way for programs (like a JavaScript frontend) to talk to your Python code.

This is your first big step into **real web development**.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand what a web server and an API is
- Set up a basic Flask app
- Define routes using `@app.route()`
- Handle **GET** and **POST** requests
- Return JSON data using `jsonify()`
- Accept input using `request.json`
- Store data in Python variables and return it via an API

---

## 🧩 Exercises

| Filename                       | Description                                           |
|-------------------------------|-------------------------------------------------------|
| 01_hello_flask.py             | Create your first Flask route                         |
| 02_return_json.py             | Return JSON instead of plain text                     |
| 03_get_request_example.py     | Handle a GET request that returns a message           |
| 04_post_request_example.py    | Accept user input with POST                           |
| 05_in_memory_storage.py       | Store data in a list and return it                   |
| 06_simple_api_get_post.py     | Combine GET and POST to create a mini-API             |
| 07_basic_crud_api.py          | Create, read, update, and delete items (CRUD)         |
| 08_route_parameters.py        | Use route parameters (like `/items/2`)                |
| 09_module_review.py           | Review all the concepts from the module               |
| 10_mini_project_todo_api.py   | Build a complete to-do list API (backend only) ✅      |

---

## 🏁 End-of-Module Challenge

🎯 **Mini Project: To-Do List API**  
Create a Flask app that lets users:
- **GET**: View all their tasks
- **POST**: Add a new task
- **PUT**: Mark a task as complete
- **DELETE**: Remove a task

The API should return clear JSON responses for each action.

Example `GET` response:
```json
[
  {"id": 1, "task": "Walk the dog", "completed": false},
  {"id": 2, "task": "Read a book", "completed": true}
]
