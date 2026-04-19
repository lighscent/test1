// test.js
// A small JavaScript utility script with a function and a command-line runner.

function multiply(a, b) {
    return a * b;
}

function describe(value) {
    return `The computed value is ${value}.`;
}

const result = multiply(6, 7);
console.log(describe(result));

