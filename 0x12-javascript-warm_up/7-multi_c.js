#!/usr/bin/node

const { argv } = require('process')
let i = 0

const num = parseInt(argv[2])

if (isNaN(num)) {
  console.log('Missing number of occurrences')
} else {
  for (i; i < num; i++) {
    console.log('C is fun')
  }
}
