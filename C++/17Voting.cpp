#include <iostream>

int main() {
  int age;
  bool citzen;
  bool registered;

  std::cout << "Please enter your age: ";
  std::cin >> age;
  std::cout << "Are you a citzen? ";
  std::cin >> citzen;
  std::cout << "Are you registered? ";
  std::cin >> registered;

  if (age >= 18 && citzen && registered) {
      std::cout << "You can vote! ";
  }
  else if (age < 18) {
      std::cout << "You are not old enough to vote";
  }
  else if (!citzen) {
      std::cout << "you are not eligible to vote";
  }
  else if (!registered) {
      std::cout << "You need to register first";
  }
  else {
      std::cout << "You have not met the requirements";
  }
  return 0;
}
