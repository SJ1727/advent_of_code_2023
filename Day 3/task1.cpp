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

    Symbol (int _x, int _y) {
        x = _x;
        y = _y;
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
                    symbols.push_back(*new Symbol(i, lineNumber));
                }
            }
        }

        lineNumber++;
    }

    bool adjecentToSymbol;

    for (int i = 0; i < numbers.size(); i++) {
        adjecentToSymbol = false;
        for (int j = 0; j < symbols.size(); j++) {
            if (abs(numbers[i].y - symbols[j].y) > 1) { continue; }

            for (int k = 0; k < numbers[i].length; k++) {
                if (abs(symbols[j].x - numbers[i].x - k) <= 1) {
                    total += numbers[i].value;
                    adjecentToSymbol = true;
                    break;
                }
            }

            if (adjecentToSymbol) { break; }
        }
    }

    cout << total;

    return 0; 
} 