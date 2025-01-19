#include <iostream>
#include <stdio.h>

int main() {
    int catage;
    int humanage;

    std::cout << "Welcome to the Cat Years program! This only works for cats older than 2 years old.\n";
    std::cout << "Enter your cat's age: ";
    std::cin >> catage;
    
    humanage = ((catage - 2) * 4) + 24;
    std::cout << "Your cat is " << ((catage - 2) * 4) + 24 << " years old in human age";

    return 0;
}