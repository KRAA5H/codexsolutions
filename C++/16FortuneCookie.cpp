#include <iostream>
#include <cstdio>
#include <cstdlib>

int main() {
    srand(time(NULL));

    std::cout << "Lucky numbers: " << std::rand() % 50 << " " << std::rand() % 50 << " " << std::rand() % 50 << " " << std::rand() % 50 << " " << std::rand() % 50 << " " << std::rand() % 50;
    return 0;
}
