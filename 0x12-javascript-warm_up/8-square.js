#!/usr/bin/node
const [arg] = process.argv.slice(2);
if (arg) {
  for (let i = 0; i < arg; i++) {
    let op = '';
    for (let j = 0; j < arg; j++) {
      op += 'x';
    }
    console.log(op);
  }
} else { console.log('Missing size'); }
