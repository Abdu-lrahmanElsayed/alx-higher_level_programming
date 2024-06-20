#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function incr(myObject) {
  let inc = myObject.value + 1;
  return inc;
}
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
