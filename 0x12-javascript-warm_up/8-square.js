#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    const shape = 'X'.repeat(num)
    console.log(shape);
  }
}
