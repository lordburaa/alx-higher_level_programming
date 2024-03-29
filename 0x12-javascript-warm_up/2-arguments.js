#!/usr/bin/node
const { argv } = require('process')

const argLength = argv.length - 2;
if (argLength <= 0) {
  console.log('No argument');
} else if (argLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
