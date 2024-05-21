﻿#include <iostream>
#include <cstdlib>
#include <ctime>

void generateRandomBinarySequence() {
    std::srand(static_cast<unsigned>(std::time(0)));

    for (int i = 0; i < 128; ++i) {
        int random_bit = std::rand() % 2;
        std::cout << random_bit;
    }
}

int main() {
    generateRandomBinarySequence();

    return 0;
}