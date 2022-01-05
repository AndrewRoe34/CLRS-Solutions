#include <stdio.h>
#include <stdlib.h>

/**
 * Adds the two binary values together
 *
 * @param A char array A
 * @param B char array B
 * @param n length of A (same as B)
 * @return pointer to char array C (has length n + 1)
 */
char *addBits(char *A, char *B, int n)
{
    char r = 0;
    char *C = (char *) malloc(sizeof(char) * (n + 1));
    for(; (n - 1) >= 0; n--) {
        char s = A[n - 1] + B[n - 1] + r;
        C[n] = s % 2;
        r = s > 1 ? 1 : 0;
    }
    C[0] = r;
}

/**
 * Starting point of application
 */
int main()
{
    char A[] = {1, 0, 1, 1};
    char B[] = {1, 1, 0, 1};
    char *C = addBits(A, B, sizeof(A) / sizeof(char)); //should be 11000
    for(int i = 0; i < 5; i++)
        printf("%d", C[i]);

    return 0;
}
