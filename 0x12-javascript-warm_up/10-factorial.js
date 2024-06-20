#!/usr/bin/node
function factorial(a) {
  let f = 1;
  for (let i = 2; i <= a; i++) {
    f *= i;
  }
  return f;
}
const [arg] = process.argv.slice(2);
const fac = factorial(arg);
console.log(fac);
