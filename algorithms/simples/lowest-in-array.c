#include <stdio.h>

int find_lowest(int arr[], int len);

int main(void)
{
    int arr[] = {53, 24, 17, 43, 87, 32, 56, 39, 11, 0, 2};
    int len = sizeof(arr) / sizeof(arr[0]);
    int lowest = find_lowest(arr, len);

    printf("%d\n", lowest);
}

int find_lowest(int arr[], int len)
{
    int lowest = arr[0];

    /*  pseudocode
        iterate the array
            check if the current value is lower than the lowest
                lowest = current
        return the lowest
    */

    for (int i = 0; i < len; i++)
    {
        if (arr[i] < lowest)
        {
            lowest = arr[i];
        }
    }
    return lowest;
}