#!/usr/bin/node

const { argv } = require('process')
const array = []

for (let i = 2; i < argv.length; i++) {
	array.push(parseInt(argv[i]));
}
const maxx = Math.max.apply(null, array);

let sd_max = 0;
for (let i = 2; i < argv.length; i++) {
	if (sd_max !== maxx) {
		if (sd_max < array[i] && array[i] != maxx) {
			sd_max = array[i];
		}
	}
}
console.log(sd_max);

