#include <stdio.h>

/**
 * Nonincreasing integer sort
 *
 * @param A array A
 * @param n length of array A
 */
void insertionSort(int *A, int n)
{
    for(int i = 1; i < n; i++) {
        int k = A[i];
        int j = i - 1;
        while(j >= 0 && k > A[j]) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = k;
    }
}

/**
 * Starting point of application
 */
int main()
{
    int A[] = {1, 2, 3, 4, 5};
    insertionSort(A, sizeof(A)/sizeof(int));
    for(int i = 0; i < 5; i++)
        printf("%d ", A[i]);

    return 0;
}
