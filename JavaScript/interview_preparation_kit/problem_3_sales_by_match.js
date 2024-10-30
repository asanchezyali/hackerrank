function jumpingOnClouds(n, ar) {
  let sockColorCount = {};
  let totalPairs = 0;
  ar.forEach((sockColor) => {
    if (sockColorCount[sockColor]) {
      sockColorCount[sockColor]++;
      if (sockColorCount[sockColor] % 2 === 0) {
        totalPairs++;
      }
    } else {
      sockColorCount[sockColor] = 1;
    }
  });
  return totalPairs;
}

const n = 9;
const ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];
console.time("Execution Time");
const result = jumpingOnClouds(n, c);
console.timeEnd("Execution Time");
console.log(result);
