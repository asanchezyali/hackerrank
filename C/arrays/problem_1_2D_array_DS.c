#include <stdio.h>
#include <stdlib.h> 
#include <time.h>

#define ROWS 6
#define COLUMNS 6

int hourglassSum(int arr_rows, int arr_columns, int** arr)
{
  int max_hourglass = -63;
  for (int i = 1; i < arr_rows - 1; i++) {
    for (int j = 1; j < arr_columns - 1; j++) {
      int current_hourglass = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1];

      if (current_hourglass > max_hourglass) {
        max_hourglass = current_hourglass;
      }
    }
  }
 return max_hourglass;
}

// Example usage
int main()
{
  int** arr = (int**)malloc(ROWS * sizeof(int*));
    for (int i = 0; i < ROWS; i++) {
        arr[i] = (int*)malloc(COLUMNS * sizeof(int));
    }

  int example[ROWS][COLUMNS] = {
    {1, 1, 1, 0, 0, 0},
    {0, 1, 0, 0, 0, 0},
    {1, 1, 1, 0, 0, 0},
    {0, 0, 2, 4, 4, 0},
    {0, 0, 0, 2, 0, 0},
    {0, 0, 1, 2, 4, 0}
  };

  for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLUMNS; j++) {
          arr[i][j] = example[i][j];
      }
  }

  clock_t start = clock();
  int result = hourglassSum(ROWS, COLUMNS, arr);
  clock_t end = clock();
  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Execution Time: %f seconds\n", execution_time);
  printf("Result: %d\n", result);
  return 0;
}