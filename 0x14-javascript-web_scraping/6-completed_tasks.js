#!/usr/bin/node

const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  // Check for errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Create an object to store the count of completed tasks by user id
  const completedTasksByUserId = {};

  // Iterate over the todos
  todos.forEach(todo => {
    // Check if the task is completed (completed property is true)
    if (todo.completed) {
      // Increment the count of completed tasks for the user id
      if (completedTasksByUserId[todo.userId] === undefined) {
        completedTasksByUserId[todo.userId] = 1;
      } else {
        completedTasksByUserId[todo.userId]++;
      }
    }
  });

  // Print the count of completed tasks by user id
  console.log(completedTasksByUserId);
});
