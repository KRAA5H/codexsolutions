#include <iostream>
#include <stdio.h>

int main() {
    std::string username;
    std::cout << "What's your name buddy: ";
    std::cin >> username;

    std::cout << "Hello " << username;
    
    int month1;
    int month2;
    int MoM;
    
    std::cout << "Enter the value for month 1 " << username << ": ";
    std::cin >> month1;
    std::cout << "Enter the value for month 2 " << username << ": ";
    std::cin >> month2;
    

    MoM = (month2 - month1)/(month1);
    MoM = MoM * 100;
    
    std::cout << "The Month-over-month (MoM) is " << MoM;
    return 0;
}
