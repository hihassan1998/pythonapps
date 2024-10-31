# 8-2 Typing Precision game.
### Documentation of Implemented Requirements
- Word and Letter Calculations

In the first part of my project, I implemented functions to calculate word and letter counts. The total_words function extracts words from input, while total_letters counts the letters in those words. The words_letters_returned function consolidates these results, providing essential data for the typing test. I aimed to create reusable functions for better readability and maintainability, simplifying debugging and enhancing clarity.

- Precision Calculations

Calculating typing precision was crucial to the project. The calculate_word_precision function compares user input against the expected text, counting correct and incorrect words, while calculate_letter_precision does the same for letters. This dual focus on precision offers a comprehensive evaluation of typing skills, with each function designed to perform its task simply and effectively.

- Data Management and Sorting Functions

I developed functions for managing data, including reading from and writing to a file and sorting results. The read_file function retrieves typing material, and the save_result function appends user performance to score.txt. Sorting functions, sort_list_of_tuples and sort_dictionary, organize results for easy understanding. This separation of concerns promotes a clean code architecture.

- Game Logic and User Interaction

The start_game function coordinates the typing test, calculating precision scores and updating results based on user input. I focused on creating an engaging user experience, structuring the game for immediate feedback. This modular approach allowed for clarity and smooth operation throughout the typing test.

### Other projects and their highlights

1. (Dynamic_URLs) Routes and HTTP Requests
Take a closer look at the app.py file to understand the intricacies of the routes and their corresponding functionalities. This section lays the foundation for handling various HTTP requests within your application.

2. (Dynamic_URLs) Building a RESTful API
Elevate your Flask application by transforming it into a petite yet powerful RESTful API. Define endpoints for different resources, implement CRUD operations, and ensure seamless handling of requests.

3. (Dynamic_URLs) Graceful Error Handling
Dive into the world of application-level error handlers. Craft responses that go beyond just error codes. Specifically, pay attention to:

404 NOT FOUND Errors: Ensure that your application responds gracefully when a requested resource is not found.

500 INTERNAL SERVER ERROR: Implement robust error handling to maintain a smooth user experience, even in the face of internal server errors.

### Additional Resources
Flask Documentation: Flask Documentation
Flask RESTful Documentation: Flask-RESTful Documentation

### Contribute:
Should you have any questions or run into challenges while navigating through this project, don't hesitate to reach out. Happy coding!