#include <iostream>
#include <string>
using namespace std;



class Bird {
    string name_, color;
    bool abilityToFly;

  public:
    Bird (string, string, bool);
    void fly(void) {
        if (abilityToFly) {
            cout << name_ << " is flying" << endl;
        } else {
            cout << name_ << " can not fly" << endl;
        }
    };
    void sing(void);
};

Bird::Bird (string name, string color, bool canFly) {
  name_ = name;
  color = color;
  abilityToFly = canFly;
}

int main() {
    Bird bird ("Birdy McBirdface", "red", true);
    bird.fly();
}