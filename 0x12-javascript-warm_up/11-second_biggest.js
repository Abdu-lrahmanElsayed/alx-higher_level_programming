#!/usr/bin/node
const args = process.argv.slice(2);
const ints = args.map(arg => parseInt(arg, 10));
const sortint = ints.sort((a, b) => b - a);
if (sortint.length > 1) {
  console.log(ints[0]);
} else { console.log(0); }
