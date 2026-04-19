// samples/c/main.c
// A simple C program that uses a math utility module.

#include <stdio.h>
#include "math_utils.h"

int main(void) {
    printf("Hello, Developer! This is the C sample app.\n");
    int value = 7;
    printf("Factorial of %d is %d\n", value, factorial(value));
    printf("Sum from 1 to %d is %d\n", value, sum_to_n(value));
    return 0;
}
