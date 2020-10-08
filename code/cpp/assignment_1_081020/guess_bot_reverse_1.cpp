#include <iostream>
#include <string>
#include <stdlib.h> /* srand, rand */
#include <time.h>   /* time */

using namespace std;

int main()
{

    srand(time(NULL));
    int guess, guesses = 0;
    int limit_low = 1;
    int limit_high = 100;
    int range = 100;
    char input = '0';
    bool not_guessed_yet = true;

    cout << "I WILL GUESS YOUR NUMBER BRO" << endl;

    while (not_guessed_yet)
    {
        guess = rand() % range + limit_low;
        cout << "Is you number " << guess << " ??" << endl;
        cout << "'s' for too small and 'b' for too big, 'c' for right number" << endl;

        cin >> input;

        switch (input)
        {
        case 's':
            limit_low = guess;
            break;

        case 'b':
            limit_high = guess;
            break;

        case 'c':
            not_guessed_yet = false;
            break;

        default:
            cout << "Wrong input" << endl;
            break;
        }

        if (not_guessed_yet)
        {
            range = limit_high - limit_low + 1;
            cout << "new limits: low " << limit_low << " high " << limit_high << " range " << range << endl;
            guesses++;
        }

        if (limit_high - limit_low < 2)
        {
            not_guessed_yet = false;
            cout << "I FAILED HARD" << endl;
        }
    };

    cout << "i needed " << guesses << " guesses to get that right" << endl;
    return 0;
}