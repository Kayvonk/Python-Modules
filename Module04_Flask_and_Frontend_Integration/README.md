# Module 04: Flask and Frontend Integration 🔄

## 🧠 Overview
Now that you’ve built your own API using Flask, it’s time to connect it to a real frontend! In this module, you’ll learn how to use **JavaScript** — the language websites use — to **send and receive data** from your Python backend using the `fetch()` API.

You won’t write any HTML or CSS here — just focus on how the frontend and backend talk to each other through the web.

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand how frontends and backends communicate via HTTP  
- Use **JavaScript `fetch()`** to make GET and POST requests  
- Send user input from a form to your Flask API  
- Display API responses in the browser using JavaScript  
- Debug simple frontend-backend connection issues  
- Build a full "data loop": input → backend → response → display  

---

## 🧩 Exercises

| Filename / Folder           | Description                                                |
|----------------------------|------------------------------------------------------------|
| 01_setup_frontend_fetch/    | Connect a basic HTML/JS file to a Flask backend            |
| 02_get_request_to_api/      | Use `fetch()` to GET data and display it on the page       |
| 03_post_form_to_api/        | Send form input from JS to Flask with POST                 |
| 04_display_response_data/   | Render backend data as HTML elements                        |
| 05_basic_error_handling/    | Handle fetch errors and bad API responses                   |
| 06_fullstack_todo_app/      | Build a simple fullstack app using Flask + JS frontend     |
| 07_module_review_quiz/      | Practice key terms: routes, fetch, response, request       |
| 08_final_project_starter/   | Set up for student’s custom app (Mood tracker, etc.)       |

---

## 🏁 End-of-Module Challenge

🎯 **Mini Project: Fullstack App with JS + Flask**  
Choose from one of the following or invent your own:  
- ✅ Mood Tracker (How are you feeling today?)  
- ✅ Favorites List (Movies, snacks, Pokémon — whatever!)  
- ✅ Pet Log (Give your pet tasks or record their activities)  

### Requirements:
- JavaScript form input that sends a POST request to Flask  
- Flask receives, stores, and returns the data  
- JavaScript fetches the data and displays it on the page  

---

## Example snippet: Sending data to backend with fetch()

```js
fetch('/api/moods', {
  method: 'POST',
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ mood: "happy" })
})
.then(response => response.json())
.then(data => {
  console.log("Server response:", data);
})
.catch(error => {
  console.error("Error:", error);
});
