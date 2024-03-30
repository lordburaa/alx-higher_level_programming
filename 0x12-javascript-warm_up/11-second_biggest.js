#!/usr/bin/node

const { argv } = require('process');

let min = argv[0];

for (let i = 1; i < argv.length; i++) {
	
	if (min < argv[i]) {
		min = argv[i]
	}
}
if (argv.length == 3 || argv.length == 2){
	min = 0;
}
console.log(min)
