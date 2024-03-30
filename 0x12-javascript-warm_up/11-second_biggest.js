#!/usr/bin/node

const { argv } = require('process');
let array = []

for (let i = 2; i < argv.length; i++) {
  	inn = parseInt(argv[i]);
	array.push(inn)
}
const tmp = array.sort();
const argLength = argv.length;
console.log(tmp);
if (argLength < 3) {
  console.log('0 printed');
} else {
  console.log('printedd in the else ocndoitoin');
  const index = argLength - 2;
  console.log(tmp[argLength]);
}
