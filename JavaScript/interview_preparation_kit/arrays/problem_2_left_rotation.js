function minimumSwaps(a, d) {
  return a.slice(d).concat(a.slice(0, d));
}

const arr = [1, 2, 3, 4, 5];
const d = 4;
console.time("Execution Time");
const result = minimumSwaps(arr, d);
console.timeEnd("Execution Time");

console.log(result);
