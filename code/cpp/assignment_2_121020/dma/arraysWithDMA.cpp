#include <iostream>

using namespace std;

void printArray(char* array)
{
    for (int i = 0; i < (sizeof(array)/sizeof(*array)); i++) {
        cout << array[i] << endl;
    }
}


// Write a function that creates an array using DMA and returns it
char *generateName()
{
    /*
    Allocate the memory on Heap using the new operator.

    You can pass the size of the memory needed using the [] operator.

    The new opertaor always returns a pointer to the first element in the
    alllocated memory.
    */
    char *newArray = new char[5];

    // You can access the memory in the ssame way as accessing an array
    
    newArray[0] = 's';
    newArray[1] = 'i';
    newArray[2] = 'm';
    newArray[3] = 'o';
    newArray[4] = 'n';

    return newArray;
}

int main()
{

    char *charArray = generateName();

    // Print the newly created array.
    cout << "\nArrays contents being received from the function" << endl;
    printArray(charArray);

    // Deallocate the allocated memory
    // Since it is an array, we need to use delete[] instead of simply delete.
    delete[] charArray;

    return 0;
}
