#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 6
#define COLUMNS 6

int *rotLeft(int a_count, int *a, int d, int *result_count)
{
  d = d % a_count;
  int *result = (int *)malloc(a_count * sizeof(int));
  if (result == NULL)
  {
    fprintf(stderr, "Error al asignar memoria\n");
    exit(1);
  }
  for (int i = 0; i < a_count; i++)
  {
    result[i] = a[(i + d) % a_count];
  }
  *result_count = a_count;
  return result;
}


int main()
{
  int a_count = 15;
  int a[15] = {33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97};
  int d = 13;
  int result_count;

  clock_t start = clock();
  int *result = rotLeft(a_count, a, d, &result_count);
  clock_t end = clock();

  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Execution Time: %f seconds\n", execution_time);
  printf("Result: ");
  for (int i = 0; i < result_count; i++)
  {
    printf("%d ", result[i]);
  }
  printf("\n");

  // Liberar memoria
  free(result);

  return 0;
}
