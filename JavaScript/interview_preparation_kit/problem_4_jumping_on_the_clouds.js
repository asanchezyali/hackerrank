/* function jumpingOnClouds(c) {
  let jumpCount = 0;
  while (c.length > 1) {
    if (c[2] === 0) {
      c.shift();
    }
    c.shift();
    jumpCount++;
  }
  return jumpCount; 
} */

function jumpingOnClouds(c) {
  let jumpCount = 0;
  let position = 0;
  while (position < c.length - 1) {
    position += (c[position + 2] === 0) ? 2 : 1;
    jumpCount++;
  }
  return jumpCount; 
}

const c = [0, 0, 0, 0, 0, 1, 0];
console.time("Execution Time");
const result = jumpingOnClouds(c);
console.timeEnd("Execution Time");
console.log(result);
