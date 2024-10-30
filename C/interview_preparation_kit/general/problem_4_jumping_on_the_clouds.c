#include <stdio.h>
#include <string.h>
#include <time.h>

int jumpingOnClouds(int c_count, int* c) {
    int jumps = 0;
    for (int i = 0; i < c_count - 1; jumps++) {
        i += (i + 2 < c_count && c[i + 2] == 0) ? 2 : 1;
    }
    return jumps;
}

// Example usage
int main()
{
  int c_count = 7;
  int c[] = {0, 0, 1, 0, 0, 1, 0};
  clock_t start = clock();
  int result = jumpingOnClouds(c_count, c);
  clock_t end = clock();
  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Execution Time: %f seconds\n", execution_time);
  printf("Result: %d\n", result);
  return 0;
}