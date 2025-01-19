#include <iostream>
#include <stdio.h>

int main() {
    double celsius;
    double fahrenheit;
    fahrenheit = 99;

    celsius = (fahrenheit - 32) / 1.8;
    std::cout << celsius;
    return 0;
}
