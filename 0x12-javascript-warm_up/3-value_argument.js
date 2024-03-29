#!/usr/bin/node

const { argv } = require('process');

if (typeof argv[2] === 'undefined') {
  console.log('No argument')
} else {
  for (let i = 2; typeof argv[i] !== 'undefined'; i++) {
  console.log(argv[i]);
  }}
