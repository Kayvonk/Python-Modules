# Module 04 Review Quiz: Flask and Frontend Integration

1. What HTTP methods are commonly used for reading and creating data?  
2. How do you send JSON data from the frontend to a Flask backend?  
3. What does the `fetch()` function return?  
4. How do you handle errors when using `fetch()` in JavaScript?  
5. Explain the difference between GET and POST requests.  
6. Why is it important to set the `Content-Type` header to `application/json` when sending JSON?  
7. How can you update the DOM with data received from an API call?  
8. What is CORS and why might you run into issues when connecting frontend and backend locally?  
9. How would you test your API endpoints without a frontend?  
10. Describe how you would build a simple frontend that displays a list of items fetched from a Flask API.

---

### Bonus challenge:

Write a simple Flask route to accept a POST request with JSON data and return a confirmation message.

```python
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    # process data here
    return jsonify({'message': 'Data received!'})
