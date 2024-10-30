function repeatedString(s, n) {
  const aCountInPattern = s.split("a").length - 1;
  const [numFullRepeats, remainingLength] = [Math.floor(n / s.length), n % s.length];
  const totalRepeats = numFullRepeats * aCountInPattern + (s.slice(0, remainingLength).split("a").length - 1);
  return totalRepeats;
}

const patternString = "a";
const totalLength = 1000000000000;

console.time("Execution Time");
const result = repeatedString(patternString, totalLength);
console.timeEnd("Execution Time");

console.log(result);
