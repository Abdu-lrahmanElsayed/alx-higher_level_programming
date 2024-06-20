#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length > 3) {
  const ints = argv.sort((a, b) => b - a);
  console.log(ints[2]);
} else { console.log(0); }
