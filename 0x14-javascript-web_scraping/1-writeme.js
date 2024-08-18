#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const txt = process.argv[3];

function writeFile (filepath, txt) {
  fs.writeFile(filepath, txt, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
}

writeFile(filepath, txt);
