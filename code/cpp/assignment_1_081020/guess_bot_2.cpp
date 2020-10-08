#include <iostream>
#include <string>
#include <stdlib.h> /* srand, rand */
#include <time.h>   /* time */

using namespace std;

int main()
{

    srand(time(NULL));

    int secret_number = rand() % 100 + 1;
    int guess = -1;
    int guesses = 0;

    cout << "GUESS MY NUMBER BRO" << endl;

    while (true)
    {
        cin >> guess;

        if (guess == secret_number)
        {
            break;
        }
        else
        {
            guesses++;
        }

        if (guess > secret_number)
        {
            cout << "to big" << endl;
        }

        if (guess < secret_number)
        {
            cout << "to small" << endl;
        }
    };

    cout << "perfekt you needed " << guesses << " guesses" << endl;
    return 0;
}