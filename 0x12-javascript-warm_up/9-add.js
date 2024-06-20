#!/usr/bin/node
function add(a, b) {
	return a + b;
}
const [arg1] = process.argv.slice(2);
const [arg2] = process.argv.slice(3);
let sum = add(+arg1, +arg2);
console.log(sum);
