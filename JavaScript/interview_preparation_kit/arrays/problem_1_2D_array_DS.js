function hourglassSum(arr) {
  let maxHourglass = -Infinity;

  for (let i = 1; i < arr.length - 1; i++) {
    for (let j = 1; j < arr[i].length - 1; j++) {
      const currentHourglass =
        arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] +
        arr[i][j] +
        arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];
      maxHourglass = Math.max(maxHourglass, currentHourglass);
    }
  }

  return maxHourglass;
}

const arr = [
  [1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0],
  [0, 0, 2, 4, 4, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 0, 1, 2, 4, 0],
];

console.time("Execution Time");
const result = hourglassSum(arr);
console.timeEnd("Execution Time");

console.log(result);
