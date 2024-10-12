#include <stdio.h>
#include <string.h>

long repeatedString(const char* s, long n) {
    long a_count_in_string = 0;
    long s_len = strlen(s);
    
    // Count 'a's in the string
    for (int i = 0; i < s_len; i++) {
        if (s[i] == 'a') {
            a_count_in_string++;
        }
    }
    
    long num_full_repeat = n / s_len;
    long remaining_length = n % s_len;
    
    long total_repeats = num_full_repeat * a_count_in_string;
    
    // Count 'a's in the remaining part
    for (int i = 0; i < remaining_length; i++) {
        if (s[i] == 'a') {
            total_repeats++;
        }
    }
    
    return total_repeats;
}

// Example usage
int main() {
    const char* s = "abcac";
    long n = 10;
    long result = repeatedString(s, n);
    printf("Result: %ld\n", result);
    return 0;
}