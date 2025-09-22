#!/usr/bin/node
const args = process.argv.slice(2);
// Can first the argument be converted to an integer?
if (isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(args[0]));
}