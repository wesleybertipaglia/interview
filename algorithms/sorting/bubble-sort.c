#include <stdio.h>

int *sort(int arr[], int len);

int main(void)
{
    int arr[] = {53, 24, 17, 43, 87, 32, 56, 39, 11, 0, 2};
    int len = sizeof(arr) / sizeof(arr[0]);
    int *sorted = sort(arr, len);

    for (int i = 0; i < len; i++)
    {
        printf("%d, ", sorted[i]);
    }
    printf("\n");
}

int *sort(int arr[], int len)
{
    // This is a placeholder implementation
    return arr;
}