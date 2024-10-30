#include <stdio.h>
#include <time.h>

int sockMerchant(int n, int ar_count, int* ar) {
  int pairs = 0;
  int socks[101] = {0};

  for (int i = 0; i < ar_count; i++)
  {
    socks[ar[i]]++;
    if (socks[ar[i]] % 2 == 0)
      pairs++;
  }

  return pairs;
}

int main()
{
  int steps = 9;
  int path[] = {10, 20, 20, 10, 10, 30, 50, 10, 20};


  clock_t start = clock();
  int result = sockMerchant(steps, 9, path);
  clock_t end = clock();
  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;

  printf("Execution Time: %f seconds\n", execution_time);
  printf(result);

  return 0;
}
