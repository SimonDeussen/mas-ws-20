#include <iostream>

using namespace std;

/*
    This program demonstrates an example of how to use arrays with functions.
*/

void fill_array(char* my_array) {
    my_array[0] = 's';
    my_array[1] = 'i';
    my_array[2] = 'm';
    my_array[3] = 'o';
    my_array[4] = 'n';
}

// To pass an array to function as a pointer.
void printArray(char* array)
{
    for (int i = 0; i < (sizeof(array)/sizeof(*array)); i++) {
        cout << array[i] << endl;
    }
}

int main()
{
    // Set the number of elements needed in the array

    char char_array[5];
    generate_array(char_array)

    // Print the garbage values created in the array
    cout << "\nArray elements without initialization:" << endl;
    printArray(char_array);

    // Initialize the array as multiples of two.
    for(int i = 0; i < NUM_OF_ITEMS; i++)
    {
        char_array[i] = 'j' + i;
    }

    // Print the initialized values in the array
    cout << "\nArray elements after initialization:" << endl;
    printArray(char_array);

    return 0;
}
