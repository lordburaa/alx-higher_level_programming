#!/usr/bin/node

const { argv } = require('process')
const array = []

for (let i = 2; i < argv.length; i++) {
  array.push(parseInt(argv[i]));
}
const maxx = Math.max.apply(null, array);

let sd_max = Number.MIN_SAFE_INTEGER;
if (argv.length > 2 ) {
for (let i = 0; i < array.length; i++) {
  if (array[i] !== maxx) {
    if (sd_max < array[i]) {
      sd_max = array[i];
    }
  }
}
}
console.log(sd_max);

