#!/usr/bin/node
const [arg] = process.argv.slice(2);
const num = +arg;
if (num) {
  for (let i = 0; i < num; i++) {
    let op = '';
    for (let j = 0; j < num; j++) {
      op += 'X';
    }
    console.log(op);
  }
} else { console.log('Missing size'); }
