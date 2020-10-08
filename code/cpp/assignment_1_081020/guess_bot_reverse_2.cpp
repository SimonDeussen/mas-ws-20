#include <iostream>
#include <string>

using namespace std;

int main()
{

    int guess, range = 0;
    int limit_low = 0;
    int limit_high = 100;
    int guesses = 0;

    char input = '0';
    bool not_guessed_yet = true;

    cout << "I WILL GUESS YOUR NUMBER BRO" << endl;

    while (not_guessed_yet)
    {
        range = limit_high - limit_low;
        guess = range / 2 + limit_low;
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
            guesses = guesses + 1;
            cout << "current number of guesses " << guesses << endl;
        }

        if (guesses > 6)
        {
            not_guessed_yet = false;
            cout << "I FAILED HARD" << endl;
        }
    };

    cout << "i needed " << guesses << " guesses to get that right" << endl;
    return 0;
}