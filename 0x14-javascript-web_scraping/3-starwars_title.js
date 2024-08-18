#!/usr/bin/node
const request = require('request');

function movieTitle (id) {
  const api = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request(api, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}

const id = process.argv[2];
movieTitle(id);
