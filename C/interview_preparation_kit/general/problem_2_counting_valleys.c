#include <stdio.h>
#include <time.h>

int countingValleys(int steps, const char *path) {
  int valleys = 0;
  int level = 0;

  for (int i = 0; i < steps; i++)
  {
    if (path[i] == 'U')
    {
      level++;
      if (level == 0)
        valleys++;
    }
    else
    {
      level--;
    }
  }

  return valleys;
}

int main()
{
  int steps = 8;
  const char *path = "UDDDUDUU";

  clock_t start = clock();
  int result = countingValleys(steps, path);
  clock_t end = clock();
  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;

  printf("Execution Time: %f seconds\n", execution_time);
  printf("Valleys: %d\n", result);

  return 0;
}
