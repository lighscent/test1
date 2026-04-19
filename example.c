// example.c
// A simple C program that prints a greeting and sums numbers from 1 to N.

#include <stdio.h>

int sum_to_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main(void) {
    printf("Hello, Developer! Welcome to C.\n");
    int n = 10;
    printf("Sum of numbers from 1 to %d is %d\n", n, sum_to_n(n));
    return 0;
}
