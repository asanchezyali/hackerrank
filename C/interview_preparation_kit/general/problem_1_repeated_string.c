#include <stdio.h>
#include <string.h>
#include <time.h>

long hourglassSum(const char *s, long n)
{
  long a_count_in_string = 0;
  long s_len = strlen(s);

  // Count 'a's in the string
  for (int i = 0; i < s_len; i++)
  {
    if (s[i] == 'a')
    {
      a_count_in_string++;
    }
  }

  long num_full_repeat = n / s_len;
  long remaining_length = n % s_len;

  long total_repeats = num_full_repeat * a_count_in_string;

  // Count 'a's in the remaining part
  for (int i = 0; i < remaining_length; i++)
  {
    if (s[i] == 'a')
    {
      total_repeats++;
    }
  }

  return total_repeats;
}

// Example usage
int main()
{
  const char *s = "abcac";
  long n = 10;
  clock_t start = clock();
  long result = hourglassSum(s, n);
  clock_t end = clock();
  double execution_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("Execution Time: %f seconds\n", execution_time);
  printf("Valleys: %d\n", result);
  printf("Result: %ld\n", result);
  return 0;
}