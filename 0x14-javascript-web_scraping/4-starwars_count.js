#!/usr/bin/node
const request = require('request');

function numberPresent (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body).results;
      const movies = data.filter((film) =>
        film.characters.some((characterUrl) =>
          characterUrl.includes('/18/'))
      );
      console.log(movies.length);
    }
  });
}

const url = process.argv[2];
numberPresent(url);
