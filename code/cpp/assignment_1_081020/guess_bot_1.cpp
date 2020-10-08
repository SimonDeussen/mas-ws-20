#include <iostream>
#include <string>
#include <stdlib.h> /* srand, rand */
#include <time.h>   /* time */

using namespace std;

int main()
{

    srand(time(NULL));

    int secret_number = rand() % 100 + 1;
    int guess = 0;

    cout << "GUESS MY NUMBER BRO" << endl;

    do
    {
        cin >> guess;

        if (guess > secret_number)
        {
            cout << "to big" << endl;
        }

        if (guess < secret_number)
        {
            cout << "to small" << endl;
        }
    } while (guess != secret_number);

    cout << "perfekt" << endl;
    return 0;
}