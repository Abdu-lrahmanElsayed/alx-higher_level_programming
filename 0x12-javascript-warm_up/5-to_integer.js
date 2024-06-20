#!/usr/bin/node
const [arg] = process.argv.slice(2);
const num = +arg;
if (num) {
  console.log('My number: ' + num);
} else { console.log('Not a number'); }
