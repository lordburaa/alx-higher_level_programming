#!/usr/bin/node
console.log('hello');
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
}
