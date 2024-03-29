#!/usr/bin/node

const { argv } = require('process');

const num = parseInt(argv[2]);

if (isNaN(argv[2])) {
	console.log('Not a number');
}
else {
	console.log('My number: ${num}');
}
