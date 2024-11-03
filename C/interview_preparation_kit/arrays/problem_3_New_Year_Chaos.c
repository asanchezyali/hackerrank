#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void minimumBribes(int q_count, int *q) {
  int bribes = 0;
  for (int i = q_count - 1; i >= 0; i--) {
    if (q[i] - (i + 1) > 2) {
      printf("Too chaotic\n");
      return;
    }
    for (int j = q[i] - 2 > 0 ? q[i] - 2 : 0; j < i; j++) {
      if (q[j] > q[i]) {
        bribes++;
      }
    }
  }
  printf("%d\n", bribes);
}

int main() {
  int q_count = 8;
  int q[8] = {5, 1, 2, 3, 7, 8, 6, 4};
  clock_t start = clock();
  minimumBribes(q_count, q);
  clock_t end = clock();

  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Execution Time: %f seconds\n", execution_time);
  return 0;
}
