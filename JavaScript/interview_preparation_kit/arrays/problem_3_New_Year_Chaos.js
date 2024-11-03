function minimumBribes(q) {
  let bribes = 0;
  let chaotic = false;
  for (let i = 0; i < q.length; i++) {
    if (q[i] - (i + 1) > 2) {
      chaotic = true;
      break;
    }
    for (let j = Math.max(0, q[i] - 2); j < i; j++) {
      if (q[j] > q[i]) {
        bribes++;
      }
    }
  }
  return chaotic ? "Too chaotic" : bribes;
}

const q = [2, 1, 5, 3, 4];
console.time("Execution Time");
const result = minimumBribes(q);
console.timeEnd("Execution Time");

console.log(result);
