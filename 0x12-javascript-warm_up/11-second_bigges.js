#!/usr/bin/node

const { argv } = require('process');

let min = 0;

for (let i = 0; i < argv.length; i++) {
	
	if (min < argv[i]) {
		min = argv[i]
	}
}
console.log(min)
