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
    /*  pseudocode
        // iterate over the array
            iterate over the array
            - the last element (because it is already in the right place)
            - 1 (because the arr starts in 0)
                if the current element is bigger than the next swap the elements
        // return the arr
    */

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len - i - 1; j++) // i=0 -> arr[n]; i=1 -> arr[n-1]
        {
            if (arr[j] > arr[j + 1]) // current > next
            {
                int temp = arr[j];
                arr[j] = arr[j + 1]; // swap elements
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}