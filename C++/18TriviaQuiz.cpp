#include <iostream>

int main() {
    int score;
    score = 0;
    std::string answer;
    std::cout << "Q1) What is the name of the world's longest river? 💧\n\n1) Missouri River\n2) Nile\n3) Amazon River\n4) Yangtze River\n";
    std::cin >> answer;

    if (answer == "2") {
        score++;
        std::cout << "Well done! Your current score is: " << score;
    }
}
