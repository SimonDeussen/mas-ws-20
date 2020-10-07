#include <iostream>
#include <string>

using namespace std;
float sum(float a, float b)
{
    return a + b;
}

float subtract(float a, float b)
{
    return a - b;
}

float mult(float a, float b)
{
    return a * b;
}

float division(float a, float b)
{
    return a / b;
}

int main()
{

    float num1 = 0;
    float num2 = 0;
    char mode = '0';

    cout << "Enter number 1:";
    cin >> num1;

    cout << "Enter number 2:";
    cin >> num2;

    cout << "Enter mode:";
    cin >> mode;

    switch (mode)
    {
    case '+':
        cout << "The sum of " << num1 << " and " << num2 << " is " << sum(num1, num2) << endl;
        break;
    case '-':
        cout << "The subtraction of " << num1 << " and " << num2 << " is " << subtract(num1, num2) << endl;
        break;
    case '*':
        cout << "The product of " << num1 << " and " << num2 << " is " << mult(num1, num2) << endl;
        break;
    case '/':
        cout << "The division of " << num1 << " and " << num2 << " is " << division(num1, num2) << endl;
        break;

    default:
        cout << "Invalid mode " << mode << endl;
    }

    return 0;
}