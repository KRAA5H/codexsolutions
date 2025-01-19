#include <iostream>
#include <stdio.h>

int main() {
    std::string username;
    std::cout << "What's your name buddy: ";
    std::cin >> username;

    std::cout << "Hello " << username << "\n\n";
    
    int month1;
    int month2;
    float MoM;
    
    std::cout << "Enter the value for month 1 " << username << ": ";
    std::cin >> month1;
    std::cout << "Enter the value for month 2 " << username << ": ";
    std::cin >> month2;
    

    MoM = (month2 - month1);
    MoM = MoM/(month1); // has to be seperate since month1, month2 are not floats; c++ is integer div by default so div by month1 has to be seperate
    MoM = MoM * 100;
    
    std::cout << "The Month-over-Month (MoM) change is " << MoM << "%.\n";

    return 0;
}
