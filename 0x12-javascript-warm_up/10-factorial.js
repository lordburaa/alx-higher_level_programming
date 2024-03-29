#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2])

function fac (a) {
  if (a === 1 || isNaN(a)) {
	  return 1;
  }

  else {
    return a*fac(a - 1)
  }
}
console.log(fac(num));
