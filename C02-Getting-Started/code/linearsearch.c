#include <stdio.h>
#include <stdlib.h>

/**
 * @param A integer A
 * @param v value being searched
 * @param n length of array A
 */
int linearSearch(int *A, int v, int n)
{
    for(int i = 0; i < n; i++) {
        if(A[i] == v)
            return i;
    }
    return -1;
}

/**
 * Starting point of application
 */
int main()
{
    int A[] = {1, 2, 3, 4, 5};
    printf("Expected:  4, Actual:  %d\n", linearSearch(A, 5, sizeof(A) / sizeof(int)));
    printf("Expected: -1, Actual: %d\n", linearSearch(A, 13, sizeof(A) / sizeof(int)));
    return 0;
}
