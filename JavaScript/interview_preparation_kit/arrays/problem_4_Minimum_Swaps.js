function minimumSwaps(arr) {
  let swaps = 0;
  for (let i = 0; i < arr.length; i++) {
    while (arr[i] !== i + 1) {
      const correctIndex = arr[i] - 1;
      [arr[i], arr[correctIndex]] = [arr[correctIndex], arr[i]];
      swaps++;
    }
  }

  return swaps;
}

const q = [2, 1, 5, 3, 4];
console.time("Execution Time");
const result = minimumSwaps(q);
console.timeEnd("Execution Time");

console.log(result);
