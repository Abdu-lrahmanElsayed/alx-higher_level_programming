#!/usr/bin/node
const fs = require('fs');
const request = require('request');

function writeApi (url, filepath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filepath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}

const url = process.argv[2];
const filepath = process.argv[3];
writeApi(url, filepath);
