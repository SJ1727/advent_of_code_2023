#include <iostream> 
#include <fstream>
#include <string>
#include <regex>

using namespace std;

struct Number {
    int x;
    int y;
    int length;
    int value;

    Number (int _x, int _y, int _length, int _value) {
        x = _x;
        y = _y;
        length = _length;
        value = _value;
    }
};

struct Symbol {
    int x;
    int y;
    char type;
    vector<Number> surrounding;

    Symbol (int _x, int _y, char _type) {
        x = _x;
        y = _y;
        type = _type;
    }

    void add_surrounding(Number num) {
        surrounding.push_back(num);
    }
};

int main() 
{ 
    int total = 0;
    std::string currentLine;
    std::ifstream file ("data.txt");

    vector<Number> numbers;
    vector<Symbol> symbols;

    int currentNumberValue = 0;
    int currentNumberLength = 0;
    int startXPos = -1;
    int lineNumber = 0;

    while (std::getline(file, currentLine)) {
        for (int i = 0; i < currentLine.length(); i++) {
            if (isdigit(currentLine[i])) {
                if (startXPos == -1) { startXPos = i; }

                currentNumberLength++;
                currentNumberValue *= 10;
                currentNumberValue += int(currentLine[i] - '0');
            } else {
                if (currentNumberLength != 0) {
                    numbers.push_back(*new Number(startXPos, lineNumber, currentNumberLength, currentNumberValue));

                    currentNumberValue = 0;
                    currentNumberLength = 0;
                    startXPos = -1;
                }

                if (currentLine[i] != '.' && currentLine[i] != '\n') {
                    symbols.push_back(*new Symbol(i, lineNumber, currentLine[i]));
                }
            }
        }

        lineNumber++;
    }

    bool touching;

    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < symbols.size(); j++) {
            touching = false;
            if (abs(numbers[i].y - symbols[j].y) > 1) { continue; }

            for (int k = 0; k < numbers[i].length; k++) {
                if (abs(symbols[j].x - numbers[i].x - k) <= 1) {
                    touching = true;
                }
            }

            if (touching) { symbols[j].add_surrounding(numbers[i]); }
        }
    }

    for (int i = 0; i < symbols.size(); i++) {
        if (symbols[i].surrounding.size() == 2) {
            total += symbols[i].surrounding[0].value * symbols[i].surrounding[1].value;
        }
    }

    cout << total;

    return 0; 
} 