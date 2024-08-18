#!/usr/bin/node
const request = require('request');

function completedTasks (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const tasks = JSON.parse(body);
      const count = {};
      tasks.forEach((task) => {
        if (task.completed) {
          const id = task.userId;
          count[id] = (count[id] || 0) + 1;
        }
      });
      console.log(count);
    }
  });
}

const url = process.argv[2];
completedTasks(url);
